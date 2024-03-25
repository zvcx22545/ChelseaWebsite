document.addEventListener("DOMContentLoaded", function(){
    const form = document.querySelector('form');
    document.getElementById("submit-btn").addEventListener("click", function(e){
        // แสดง Swal.fire
        Swal.fire({
            title: 'กำลังบันทึกข้อมูลกรุณารอสักครู่',
            allowOutsideClick: false,
  
            didOpen: () => {
                Swal.showLoading();
            },
            willClose: () => {
                // ทำอะไรก็ได้เมื่อ Swal.fire ปิด (ถ้าจำเป็น)
            }
        });
  
        form.submit(); // ส่งฟอร์มไปยังเซิร์ฟเวอร์
    });
  });