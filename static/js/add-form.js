document.addEventListener("DOMContentLoaded", () => {
  function previewImage(Imginput, ImgPreview) {
    var fileInput = document.getElementById(Imginput);
    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
      var img = document.createElement("img");
      img.src = reader.result;
      img.style.maxWidth = "20%";
      img.style.maxHeight = "20%";
      img.style.display = "flex";
      img.style.margin = "auto";
      img.style.marginTop = "2rem";
      img.style.marginBottom = "2rem";

      var container = document.getElementById(ImgPreview);
      container.innerHTML = "";
      container.appendChild(img);

      // Add a click event listener to the image for larger preview
      img.addEventListener("click", function () {
        var largeImg = document.createElement("img");
        largeImg.src = reader.result;
        largeImg.style.maxWidth = "60%";
        largeImg.style.maxHeight = "60%";
        largeImg.style.display = "block";
        largeImg.style.margin = "auto";
        largeImg.style.marginTop = "2rem";
        largeImg.style.marginBottom = "2rem";

        // Create a modal or a larger preview container to display the image
        var modal = document.createElement("div");
        modal.style.position = "fixed";
        modal.style.top = "0";
        modal.style.left = "0";
        modal.style.width = "100%";
        modal.style.height = "100%";
        modal.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
        modal.style.display = "flex";
        modal.style.alignItems = "center";
        modal.style.justifyContent = "center";
        modal.style.zIndex = "9999";

        modal.appendChild(largeImg);

        // Add a click event listener to close the modal when clicked outside the image
        modal.addEventListener("click", function (event) {
          if (event.target === modal) {
            modal.style.display = "none";
          }
        });

        document.body.appendChild(modal);
      });
    };

    if (file) {
      reader.readAsDataURL(file);
    } else {
      document.getElementById(ImgPreview).innerHTML = "";
    }
  }

  // Event listener for the upload button 1
  function addEventListeners() {
    const fileUpload2 = document.getElementById("file-upload-2");
    const uploadButton2 = document.getElementById("upload-button-2");
    const fileUpload3 = document.getElementById("file-upload-3");
    const uploadButton3 = document.getElementById("upload-button-3");
    const fileUpload0 = document.getElementById("file-upload-0");
    const uploadButton0 = document.getElementById("upload-button-0");
    const fileUpload4 = document.getElementById("file-upload-4");
    const uploadButton4 = document.getElementById("upload-button-4");
    // payment preview
    const uploadPayment = document.getElementById("upload-payment");
    const uploadPaymentButton = document.getElementById(
      "upload-payment-button"
    );

    if (fileUpload2 && uploadButton2) {
      fileUpload2.addEventListener("change", () => {
        previewImage("file-upload-2", "image-preview-container-2");
      });

      uploadButton2.addEventListener("click", () => {
        fileUpload2.click();
      });
    }
    if (fileUpload3 && uploadButton3) {
      fileUpload3.addEventListener("change", () => {
        previewImage("file-upload-3", "image-preview-container-3");
      });

      uploadButton3.addEventListener("click", () => {
        fileUpload3.click();
      });
    }
    if (fileUpload0 && uploadButton0) {
      fileUpload0.addEventListener("change", () => {
        previewImage("file-upload-0", "image-preview-container-0");
      });

      uploadButton0.addEventListener("click", () => {
        fileUpload0.click();
      });
    }
    if (fileUpload4 && uploadButton4) {
      fileUpload4.addEventListener("change", () => {
        previewImage("file-upload-4", "image-preview-container-4");
      });

      uploadButton4.addEventListener("click", () => {
        fileUpload4.click();
      });
    }
    if (uploadPayment && uploadPaymentButton) {
      uploadPayment.addEventListener("change", () => {
        previewImage("upload-payment", "image-preview");
      });

      uploadPaymentButton.addEventListener("click", () => {
        uploadPayment.click();
      });
    }
  }
  addEventListeners();
 
});

