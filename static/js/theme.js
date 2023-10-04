// Get references to the button and the body element
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Check if a user preference is already set in localStorage
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
  body.classList.add(currentTheme); // Apply saved theme
}

// Function to toggle between dark and light mode
function toggleTheme() {
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
    localStorage.setItem('theme', 'light-mode');
  } else {
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark-mode');
  }
}

// Add click event listener to the button
themeToggle.addEventListener('click', toggleTheme);
