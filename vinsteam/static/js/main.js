$(document).ready(function () {
  $(".slider_top_main").slick({
    dots: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    speed: 500,
    autoplay: true,
    autoplaySpeed: 3000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {},
      },
      {
        breakpoint: 600,
        settings: {
          arrows: false,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
        },
      },
    ],
  });
});

$(document).ready(function () {
  // Инициализация слайдера
  $(".foto_random_main").slick({
    dots: true,
    slidesToShow: 1,
    slidesToScroll: 2,
    infinite: true,
    arrows: true,
    centerMode: true,
    variableWidth: true,
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 2,
        },
      },
    ],
  });
  // Обработчик кликов на изображениях
  $(".slider-image").click(function () {
    // Получаем ссылку на изображение
    var imageSrc = $(this).attr("src");

    // Устанавливаем ссылку на изображение в блоке на весь экран
    $("#fullscreen-image-src").attr("src", imageSrc);
    $("#fullscreen-image").addClass("active");

    // Показываем блок на весь экран
    $("#fullscreen-image").show();
  });

  // Обработчик кликов на кнопке закрытия
  $("#close-fullscreen-image").click(function () {
    // Скрываем блок на весь экран
    $("#fullscreen-image").hide();
  });
});
$(document).ready(function () {
  $(".reviews_ul").slick({
    dots: true,
    slidesToShow: 2,
    slidesToScroll: 2,
    arrows: true,
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });
});
// наведение на главное меню
const headerItemDivs = document.querySelectorAll(".header_item_div_main");

headerItemDivs.forEach((headerItemDiv) => {
  headerItemDiv.addEventListener("mouseover", () => {
    headerItemDiv.classList.add("active");
  });

  headerItemDiv.addEventListener("mouseout", () => {
    headerItemDiv.classList.remove("active");
  });
});
$(document).ready(function () {
  $("#lk_top").click(function () {
    $("#authModal").toggleClass("active");
  });
});

// $(document).ready(function () {
//   $("#version_no_see").click(function () {
//     $("#body_id").addClass("see");
//     $("#version_no_see_x1").addClass("active");
//     $("#version_no_see_x2").removeClass("active");
//   });
// });
// $(document).ready(function () {
//   $("#version_yes_see").click(function () {
//     $("#body_id").removeClass("see");
//     $("#body_id").removeClass("see_x2");
//   });
// });
// $(document).ready(function () {
//   $("#version_no_see_x2").click(function () {
//     $("#version_no_see_x1").removeClass("active");
//     $(this).addClass("active");
//     $("#body_id").addClass("see_x2");
//   });
// });
// $(document).ready(function () {
//   $("#version_no_see_x1").click(function () {
//     $("#version_no_see_x2").removeClass("active");
//     $(this).addClass("active");
//     $("#body_id").removeClass("see_x2");
//     $("#body_id").addClass("see");
//   });
// });
$(document).ready(function () {
  $(".mobile_header_item").click(function () {
    $(this).toggleClass("active");
  });
});
$(document).ready(function () {
  $(".btn_all").click(function () {
    $('.div_101_p').addClass("active");
    $('.btn_no').addClass("active");
    $(this).addClass("active");
  });
});
$(document).ready(function() {
  $(".quest_btn").click(function() {
    $(this).parent(".quest_item").toggleClass("active");
  });
});

$(document).ready(function () {
  $(".btn_no").click(function () {
    $('.div_101_p').removeClass("active");
    $('.btn_all').removeClass("active");
    $(this).removeClass("active");
  });
});
$(document).ready(function () {
  $(".write_me").click(function () {
    $("#write_me").toggleClass("active");
  });
});
$(document).ready(function () {
  $(".show_more_review").click(function () {
    $("#review_full").toggleClass("active");
  });
});
$(document).ready(function () {
  $(".form_group_reg").click(function () {
    $("#authModal").removeClass("active");
    $("#authModalreg").addClass("active");
  });
});
$(document).ready(function () {
  $(".span_prev").click(function () {
    $("#authModalreg").removeClass("active");
    $("#authModal").addClass("active");
  });
});
$(document).ready(function () {
  $(".close_modal").click(function () {
    $(".modal_reg").removeClass("active");
  });
});
$(document).ready(function () {
  $(".review_write_btn").click(function () {
    $("#review_write").addClass("active");
  });
});

// получаем элемент header_down_main
const headerDownMain = document.querySelector(".header_down_main_none");

// добавляем обработчик события scroll к window
window.addEventListener("scroll", function () {
  // проверяем, прокрутили ли мы страницу на 300px сверху
  if (
    window.pageYOffset >= 300 &&
    !headerDownMain.classList.contains("active")
  ) {
    // если да, и класс "active" еще не добавлен, то добавляем его к элементу header_down_main
    headerDownMain.classList.add("active");
  } else if (
    window.pageYOffset < 300 &&
    headerDownMain.classList.contains("active")
  ) {
    // если нет, и класс "active" уже добавлен, то удаляем его у элемента header_down_main
    headerDownMain.classList.remove("active");
  }
});

$(document).ready(function () {
  // Скрыть все списки подкатегорий и товаров при загрузке страницы
  $(".category_pod, .category_item").hide();

  // При клике на категорию
  $(".cat_gl").click(function () {
    // Скрыть все списки подкатегорий и товаров, кроме тех, что относятся к выбранной категории
    $(".category_pod, .category_item")
      .not($(this).nextAll(".category_pod, .category_item"))
      .slideUp();
    // Раскрыть список подкатегорий текущей категории
    $(this).next(".category_pod").slideToggle();
  });

  // При клике на подкатегорию
  $(".category_pod p").click(function () {
    // Скрыть все списки товаров, кроме тех, что относятся к выбранной подкатегории
    $(".category_item").not($(this).next(".category_item")).slideUp();
    // Раскрыть список товаров текущей подкатегории
    $(this).next(".category_item").slideToggle();
  });
});

// Выпадающее меню

// отправка сообщения письма
// const form = document.getElementById("writeForm");
// form.addEventListener("submit", (event) => {
//   event.preventDefault();
//   const xhr = new XMLHttpRequest();
//   xhr.open("POST", form.action);
//   xhr.setRequestHeader(
//     "X-CSRFToken",
//     form.querySelector("[name=csrfmiddlewaretoken]").value
//   );
//   xhr.onreadystatechange = function () {
//     if (xhr.readyState === 4) {
//       if (xhr.status === 200) {
//         setTimeout(() => {
//           document.querySelector("#write_me").classList.remove("active");
//           document.querySelector("#write_ok").classList.add("active");
//         }, 500);
//         form.reset();
//       } else if (xhr.status === 400) {
//         const errorResponse = JSON.parse(xhr.responseText);
//         const errorMessage = errorResponse.error;
//         document.querySelector(".error_login").textContent = errorMessage;
//       } else if (xhr.status === 500) {
//         const errorResponse = JSON.parse(xhr.responseText);
//         const errorMessage = errorResponse.error;
//         alert(errorMessage);
//       } else {
//         alert("Ошибка отправки сообщения");
//       }
//     }
//   };
//   const formData = new FormData(form);
//   xhr.send(formData);
// });

// отправка сообщения письма 2
var form = document.getElementById("writeForm_2");
if (form) {
  form.addEventListener("submit", function(event) {
    event.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", form.action);
    xhr.setRequestHeader("X-CSRFToken", form.querySelector("[name=csrfmiddlewaretoken]").value);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          setTimeout(function() {
            document.querySelector("#write_me").classList.remove("active");
            document.querySelector("#write_ok").classList.add("active");
          }, 500);
          form.reset();
        } else if (xhr.status === 400) {
          var errorResponse = JSON.parse(xhr.responseText);
          var errors = errorResponse.errors;
          if (errors) {
            var errorMessage = "";
            for (var field in errors) {
              errorMessage += decodeURIComponent(errors[field]);
            }
            document.querySelector(".error_login").textContent = errorMessage;
          }
        } else if (xhr.status === 500) {
          var errorResponse = JSON.parse(xhr.responseText);
          var errorMessage = errorResponse.errors;
          alert(errorMessage);
        } else {
          alert("Ошибка отправки сообщения");
        }
      }
    };
    var formData = new FormData(form);
    xhr.send(formData);
  });
}




// отправка отзыва общего
$(document).ready(function () {
  $("#review-form").submit(function (event) {
    event.preventDefault();
    var form = $(this);
    submitForm(form);
  });
});

function submitForm(form) {
  var url = form.attr("action");
  var data = form.serialize();
  data += "&username=" + encodeURIComponent($("#id_name").val());
  $.ajax({
    url: url,
    type: "POST",
    data: data,
    success: function (response) {
      console.log(response);
      form.trigger("reset"); // очищаем содержимое формы
      $("#review_write").removeClass("active");
      $("#review_ok").addClass("active");
    },
    error: function (xhr) {
      var errors = xhr.responseJSON.errors;
      var errorHtml = "";
      for (var field in errors) {
        errorHtml += "<p>" + errors[field] + "</p>";
      }
      $("#review-form-errors").html(errorHtml);
    },
  });
}


// получить весь отзыв
$(document).ready(function () {
  $(".show_more_review").click(function (event) {
    event.preventDefault();
    var review_id = $(this).data("review-id");
    $.ajax({
      url: "/reviews/get_full_review/",
      data: { review_id: review_id },
      success: function (response) {
        var review = response["review"];
        $("#review_full .review_date").text(review.created_at);
        $("#review_full .review_name").text(review.name);
        $("#review_full .review_text").text(review.text);
        // $('#review_full').modal('show');
      },
    });
  });
});

// работает но не обновляет
// const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
// const logoutForm = document.querySelector('#logoutForm');

// logoutForm.addEventListener('submit', function(e) {
//   e.preventDefault();
//   const xhr = new XMLHttpRequest();
//   xhr.open('POST', logoutForm.action);
//   xhr.setRequestHeader('X-CSRFToken', csrfToken);
//   xhr.onreadystatechange = function() {
//     if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
//       const response = JSON.parse(xhr.responseText);
//       if (response.success) {
//         window.location.reload();
//       } else {
//         console.log(response.errors);
//       }
//     }
//   };
//   xhr.send();
// });
