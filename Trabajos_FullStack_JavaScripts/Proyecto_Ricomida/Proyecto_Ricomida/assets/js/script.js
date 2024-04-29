$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();

  $(".carousel").carousel();

  $("#element").tooltip("show");

  $(".title1").dblclick(function () {
    $(this).css({
      color: "red",
    });
  });

  $(".title2").dblclick(function () {
    $(this).css({
      color: "red",
    });
  });

  $(".card-title1, .card-title2, .card-title3").click(function () {
    $(".card-text1").toggle();
    $(".card-text2").toggle();
    $(".card-text3").toggle();
  });

/*  $(".card-title2").click(function () {
    $(".card-text2").toggle();
  });

  $(".card-title3").click(function () {
    $(".card-text3").toggle();
  });
 */

  $("#envia").click(function(){
    alert("El correo fue enviado correctamente...")
  });
});
