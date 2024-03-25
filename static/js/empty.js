document.addEventListener("DOMContentLoaded", function () {
  // Function to set the height of .empty
  function setEmptyHeight() {
    const navbarHeight = document.querySelector('.navbar').offsetHeight;
    document.querySelector('.empty').style.height = `${navbarHeight}px`;
  }

  // Initial setup
  setEmptyHeight();

  // Event listener for window resize
  window.addEventListener('resize', setEmptyHeight);
  
});

document.addEventListener('DOMContentLoaded', function() {
  var selectElement = document.getElementById('stadium-select');
  var arrowIcon = document.querySelector('.angledown');
  var originalRotation = window.getComputedStyle(arrowIcon).getPropertyValue('transform');


  // Function to reset arrow rotation
  function resetArrowRotation() {
      arrowIcon.classList.remove('rotate-arrow');
      void arrowIcon.offsetWidth; // Trigger reflow to restart animation
      arrowIcon.classList.add('rotate-arrow');
  }

  // Reset arrow rotation when select option is changed
  selectElement.addEventListener('change', resetArrowRotation);
  

  // Reset arrow rotation when arrow icon is clicked
  arrowIcon.addEventListener('click', resetArrowRotation);
});