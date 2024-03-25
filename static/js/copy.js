
document.addEventListener("DOMContentLoaded", () => {
  // Attach the function to the checkboxes
  function copyToClipboard(elementId) {
    var textToCopy = document.getElementById(elementId).innerText.trim();
    console.log("copyToClipboard function called with elementId:", elementId);

    // Modern approach with Clipboard API
    if (navigator.clipboard) {
      navigator.clipboard
        .writeText(textToCopy)
        .then(function () {
          console.log("Text successfully copied to clipboard");
          showAlert("success", "คัดลอกสำเร็จแล้ว", "success");
        })
        .catch(function (err) {
          console.error("Could not copy text: ", err);
        });
    } else {
      // Fallback for older browsers
      var inputElement = document.createElement("input");
      inputElement.setAttribute("value", textToCopy);
      document.body.appendChild(inputElement);
      inputElement.select();
      inputElement.setSelectionRange(0, 99999); // For mobile devices

      var successful = document.execCommand("copy");
      document.body.removeChild(inputElement);

      if (successful) {
        console.log("Text successfully copied to clipboard");
        showAlert("success", "คัดลอกสำเร็จแล้ว", "success");
      } else {
        console.error("Failed to copy text.");
      }
    }
  }
  var copyIcon = document.querySelector(".bi-copy");
  if (copyIcon) {
    console.log("Attaching event listener to copy icon");
    copyIcon.addEventListener("click", function () {
      copyToClipboard("account-number");
    });
  } else {
    console.log("Copy icon not found");
  }

  // const paymentValue = (Paymentinput) => {
  //   let paymentInput = document.getElementById(Paymentinput);
  //   if (paymentInput.files.length > 0) {
  //     showAlert("ทำรายการสำเร็จ", "อัพโหลดสลิปสำเร็จ", "success");
  //   } else {
  //     showAlert("แจ้งเตือน!", "กรุณาอัพโหลดสลิปชำระเงิน", "error");
  //   }
  // };

  // let checkPayment = document.getElementById("load4"); // Corrected variable name
  // checkPayment.addEventListener("click", function () {
  //   paymentValue("upload-payment");
  // });
});
