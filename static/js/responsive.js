function toggleHam(x) {
    x.classList.toggle("change");

    let myMenu = document.getElementById('myMenu');
    if(myMenu.className === 'menu')
    {
        myMenu.className += ' menu-active';
    } else
    {
        myMenu.className = 'menu';
    }
  }

  
// Modal popup Youtube
  // Get modal elements
  const modalyoutube = document.getElementById('videoModal');
  const closeModalBtn = document.getElementById('closeModalBtn');

  // Function to open the modal
  function openModal() {
      modalyoutube.style.display = 'block';
  }

  // Function to close the modalyoutube
  function closeModal() {
      modalyoutube.style.display = 'none';
  }

  // Event listener for closing the modalyoutube
  closeModalBtn.addEventListener('click', closeModal);

  // Close the modalyoutube if the user clicks outside of it
//   window.addEventListener('click', (e) => {
//       if (e.target === modalyoutube) {
//           closeModal();
//       }
//   });

  // Automatically open the modal when the page loads
  window.addEventListener('load', openModal);

  