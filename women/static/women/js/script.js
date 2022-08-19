/* Переключение между отображением и скрытием ссылок меню навигации, когда пользователь нажимает на значок меню/панели гамбургеров */
function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }