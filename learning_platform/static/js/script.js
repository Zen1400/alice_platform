// static/js/script.js

document.addEventListener("DOMContentLoaded", function () {
  // Example of smooth scrolling when clicking navigation links that reference anchors on the same page
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener("click", function(e) {
          e.preventDefault();
          const targetElement = document.querySelector(this.getAttribute("href"));
          if (targetElement) {
              targetElement.scrollIntoView({ behavior: "smooth", block: "start" });
          }
      });
  });
});
