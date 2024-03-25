// Function to uncheck all toggle inputs except the one passed as an argument
function uncheckOthers(currentToggleId) {
  // Get all toggle inputs
  const toggleInputs = document.querySelectorAll('.toggle-input');

  // Loop over the toggle inputs
  toggleInputs.forEach(input => {
    // If the input is not the one that was just changed, uncheck it
    if (input.id !== currentToggleId) {
      input.checked = false;
      const content = input.nextElementSibling.nextElementSibling;
      content.style.display = 'none'; // Hide the content of the unchecked toggles
    }
  });
}

// Add event listeners to the toggle inputs
document.addEventListener('DOMContentLoaded', function() {
  // Get all toggle inputs
  const toggleInputs = document.querySelectorAll('.toggle-input');
  // Loop over the toggle inputs to add change event listeners
  toggleInputs.forEach(input => {
    input.addEventListener('change', function() {
      // When a toggle is changed, uncheck all others
      uncheckOthers(this.id);

      // Toggle the display of the current toggle's content
      const content = this.nextElementSibling.nextElementSibling;
      if (this.checked) {
        content.style.display = 'block'; // Show the content if the toggle is checked
      } else {
        content.style.display = 'none'; // Hide the content if the toggle is unchecked
        dataRegis.style.marginTop = '0';
      }
    });
  });
});
