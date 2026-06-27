// Conduvia — MathJax 3 config for pymdownx.arithmatex (generic mode).
// Renders the chemistry/process equations that previously printed as literal LaTeX.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-typeset on MkDocs Material's instant-navigation page loads.
if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.typesetClear && MathJax.typesetClear();
      MathJax.texReset && MathJax.texReset();
      MathJax.typesetPromise();
    }
  });
}
