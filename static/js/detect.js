function showAlert(title, text, icon) {
  Swal.fire({
    title: title,
    text: text,
    icon: icon || "error",
    confirmButtonText: "ตกลง",
  });
}
document.addEventListener("DOMContentLoaded", () => {
  const CheckInputValue = (submitid) => {
    const submitButton = document.getElementById(submitid);
    if (submitButton) {
      submitButton.addEventListener("click", function (event) {
        var requiredFields = document.querySelectorAll(".required-field");
        var allFieldsFilled = true;

        // Check each field
        for (var i = 0; i < requiredFields.length; i++) {
          if (requiredFields[i].value.trim() === "") {
            allFieldsFilled = false;
            break;
          }
        }

        // If any field is empty, show SweetAlert2 alert and prevent form submission
        if (!allFieldsFilled) {
          event.preventDefault();
          Swal.fire({
            icon: "error",
            title: "แจ้งเตือน",
            text: "กรุณากรอกข้อมูลให้ครบถ้วน!",
          });
        }
      });
    } else {
      console.error("Submit button not found:", submitid);
    }
  };
  try {
  CheckInputValue("load2");
  CheckInputValue("load3");
  CheckInputValue("load4");
} catch (error) {
  console.error("Error attaching event listener:", error);
}

  function setupInputValidation(teamNameId, Nameid, phoneCaptainId) {
    var Teamname = document.getElementById(teamNameId);
    var Captain = document.getElementById(Nameid);
    var phoneCaptain = document.getElementById(phoneCaptainId);
    //   var emailCaptian = document.querySelector('input[name="emailCaptian"]');
    //   var AgeInput = document.querySelector('input[name="age"]');

    function validateInput(inputField, errorMessage) {
      // Regular expression that matches anything that is not a-Z, Thai characters, or whitespace

      var regex = /[^A-Za-zก-๙\s]/g;

      if (regex.test(inputField.value)) {
        showAlert("ไม่อนุญาต!", errorMessage, "error");

        // Remove invalid characters

        inputField.value = inputField.value.replace(regex, "");
      }
    }

    if (Teamname) {
      Teamname.oninput = function () {
        validateInput(this, "ใส่เฉพาะตัวอักษร A-z และ ก-ฮ เท่านั้น!!");
      };
    }

    if (Captain) {
      Captain.oninput = function () {
        validateInput(this, "ใส่เฉพาะตัวอักษร A-z และ ก-ฮ เท่านั้น!!");
      };
    }

    // Function to validate the telephone input

    if (phoneCaptain) {
      phoneCaptain.oninput = function () {
        this.value = this.value.replace(/\D/g, "");
      };
      phoneCaptain.onblur = function () {
        var value = this.value;
        if (value.length !== 10) {
          showAlert("แจ้งเตือน!", "กรุณากรอกเบอร์โทรให้ถูกต้อง", "error");
          this.value = value.slice(0, 10);
        }  
       
      };
    }
  }
  

  setupInputValidation("Teamname", "Captain", "phoneCaptain");
  setupInputValidation(null, "nameplayer", "phoneplayer");
  setupInputValidation(null, "nameplayer-2", "phoneplayer-2");
  setupInputValidation(null, "nameplayer-3", "phoneplayer-3");
  setupInputValidation(null, "nameplayer-4", "phoneplayer-4");

  //  check value form input

  function checkInputs(idinput1, idinput2, idinput3) {
    let input1 = document.getElementById(idinput1);
    let input2 = document.getElementById(idinput2);
    let input3 = document.getElementById(idinput3);

    // Check if the first input is not empty.
    if (input1.value !== "") {
      // Make input2 and input3 required.
      input2.setAttribute("required", "");
      input3.setAttribute("required", "");

      // Check if input2 or input3 is empty and show an alert if they are.
      if (input2.value === "" || input3.value === "") {
        showAlert("แจ้งเตือน!", "กรุณากรอกข้อมูลให้ครบถ้วน!", "error");
        return false; // Prevent form submission
      }
    } else {
      // If input1 is empty, remove the required attribute from input2 and input3.
      input2.removeAttribute("required");
      input3.removeAttribute("required");
    }

    // If everything is filled out, allow form submission.
    return true;
  }
  // แสดงข้อความเมื่อคลิกปุ่ม "ถัดไป"
  let button = document.querySelector(".next-2");
  button.addEventListener("click", function () {
    checkInputs("nameplayer-2", "dateplayer-2", "phoneplayer-2");
  });
  let checkinput3 = document.querySelector(".next-2");
  checkinput3.addEventListener("click", function () {
    checkInputs("nameplayer-3", "dateplayer-3", "phoneplayer-3");
  });
  let checkinput4 = document.querySelector(".next-2");
  checkinput3.addEventListener("click", function () {
    checkInputs("nameplayer-4", "dateplayer-4", "phoneplayer-4");
  });

 
});

function blockThaiInput(event) {
  var regex = /[^\u0E00-\u0E7F]/g; // Regular expression to match non-Thai characters
  if (!regex.test(event.key)) {
    event.preventDefault(); // Prevent Thai characters
    showAlert(
      "แจ้งเตือน!",
      "ไม่สามารถใส่ภาษาไทยได้!",
      "error"
    );
  }
}


document.addEventListener("DOMContentLoaded", () => {
   // Attach the function to the input element
   var inputElement = document.getElementById('LindID');
   inputElement.addEventListener('keypress', blockThaiInput);
   var inputElement = document.getElementById('emailCaptian');
   inputElement.addEventListener('keypress', blockThaiInput);
  const paymentValue = (Paymentinput) => {
    let paymentInput = document.getElementById(Paymentinput);
    if (paymentInput.files.length > 0) {
      console.log("Payment is successfuly")
    } else {
      showAlert("แจ้งเตือน!", "กรุณาอัพโหลดสลิปชำระเงิน", "error");
    }
  };

  let checkPayment = document.getElementById("load4"); // Corrected variable name
  checkPayment.addEventListener("click", function () {
    paymentValue("upload-payment");
  });

  

  // Attach the click event listener to the copy icon
 

});



  // else if (/(\d{3,})\1+/.test(value)) {
  //   showAlert(
  //     "แจ้งเตือน!",
  //     "เบอร์โทรศัพท์ไม่สามารถมีลำดับตัวเลขที่ซ้ำกันได้!",
  //     "error"
  //   );
  //   this.value = "";
  // }
  // else if (/(\d)\1{6,}/.test(value)) {
  //   showAlert(
  //     "แจ้งเตือน!",
  //     "เบอร์โทรศัพท์ไม่สามารถมีตัวเลขที่ซ้ำกันมากกว่า 6 ตัวได้!",
  //     "error"
  //   );
  //   this.value = "";
  // }
