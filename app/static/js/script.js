 // Toggle between Light Mode and Dark Mode
 function toggleDarkMode() {
  const body = document.body;
  // body.classList.toggle('dark-mode');
  const darkModeToggle = document.getElementById('darkModeToggle');
  body.classList.toggle('dark-mode');
  darkModeToggle.classList.toggle('active');
  list = body.classList;
  console.log(list);
  // Update icon based on mode
  const darkModeIcon = document.querySelector('.dark-mode-icon');
  const iconClass = body.classList.contains('dark-mode') ? 'bxs-sun' : 'bxs-moon';
  darkModeIcon.classList.remove('bxs-moon', 'bxs-sun');
  darkModeIcon.classList.add(iconClass);
}
