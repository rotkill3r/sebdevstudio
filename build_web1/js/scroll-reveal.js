(function() {
  'use strict';

  const revealEls = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .stagger');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -20px 0px'
  });

  revealEls.forEach(el => observer.observe(el));

  setTimeout(() => {
    revealEls.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        el.classList.add('visible');
      }
    });
  }, 100);
})();
