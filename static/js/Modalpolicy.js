function checkOnlyOne(checkboxId) {
  if (checkboxId === "acceptPolicy") {
    document.getElementById("rejectPolicy").checked = false;
  } else if (checkboxId === "rejectPolicy") {
    document.getElementById("acceptPolicy").checked = false;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  // Attach the function to the checkboxes

  var modal = document.getElementById("policyModal");

  // Show the modal
  modal.style.display = "block";

  // Handle the policy confirmation
  document.getElementById("confirmPolicy").onclick = function () {
    var accept = document.getElementById("acceptPolicy").checked;
    var reject = document.getElementById("rejectPolicy").checked;

    if (accept) {
      modal.style.display = "none";
      // You can enable the form here if it's disabled
    } else if (reject) {
      window.location.href = "/home";

      // Handle the rejection case, maybe redirect or show a message
    }
  };
  document.getElementById("acceptPolicy").onclick = function () {
    checkOnlyOne("acceptPolicy");
  };
  document.getElementById("rejectPolicy").onclick = function () {
    checkOnlyOne("rejectPolicy");
  };

  // ====================================================================================================================
});
