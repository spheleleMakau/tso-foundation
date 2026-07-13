document.addEventListener('DOMContentLoaded', function () {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  const links = document.querySelectorAll('.nav-links a');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      const expanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!expanded));
      navToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
      document.body.classList.toggle('nav-open', !expanded);
    });

    document.addEventListener('click', function (event) {
      if (!navLinks.contains(event.target) && !navToggle.contains(event.target)) {
        if (navLinks.classList.contains('active')) {
          navLinks.classList.remove('active');
          navToggle.classList.remove('active');
          navToggle.setAttribute('aria-expanded', 'false');
          document.body.classList.remove('nav-open');
        }
      }
    });
  }

  links.forEach(function (link) {
    link.addEventListener('click', function () {
      navLinks?.classList.remove('active');
      navToggle?.classList.remove('active');
      navToggle?.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-open');
    });
  });
});
