document.addEventListener('DOMContentLoaded', function() {
  var viewDetailsButtons = document.querySelectorAll('.view-details-btn');

  // เปลี่ยนเป็นการค้นหาทุก modal โดยใช้ class
  var modals = document.querySelectorAll('.modal3');

  viewDetailsButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          var teamId = this.getAttribute('data-team-id');
          // ปรับแสดงข้อมูลของทีมตาม teamId ใน modalContent ตรงนี้
          var modal = document.getElementById('myModal-' + teamId);
          modal.style.display = 'block';
      });
  });

  // Loop ผ่านทุก modals เพื่อเพิ่ม event listener ให้กับปุ่มปิด
  modals.forEach(function(modal) {
      var closeBtn = modal.querySelector('.close');
      closeBtn.addEventListener('click', function() {
          modal.style.display = 'none';
      });
  });
});
