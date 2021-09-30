$("#full-screen").on("click", function() {
    if ($("#full-screen2").hasClass("display_none")) {
        $("#full-screen2").addClass("display_absolute").removeClass("display_none")
        $("#full-screen").addClass("display_none")
        $(".overflow").addClass("full")
        $(".controls").addClass("full-con")
    } else {
        $("#full-screen2").removeClass("display_absolute").addClass("display_none")
    }
})

$("#full-screen2").on("click", function() {
    if ($("#full-screen").hasClass("display_none")) {
        $("#full-screen").addClass("display_absolute").removeClass("display_none")
        $("#full-screen2").addClass("display_none")
        $(".overflow").removeClass("full")
        $(".controls").removeClass("full-con")
    } else {
        $("#full-screen").removeClass("display_absolute").addClass("display_none")
    }
})

$("td").on("dblclick", function() {
    if ($(".modal-form").hasClass("display_none")) {
        $(".modal-form").addClass("display_absolute").removeClass("display_none")
    } else {
        $(".modal-form").removeClass("display_absolute").addClass("display_none")
    }
})

$(".times").on("click", function() {
    if ($(".modal-form").hasClass("display_absolute")) {
        $(".modal-form").addClass("display_none").removeClass("display_absolute")
    } else {
        $(".modal-form").removeClass("display_absolute").addClass("display_none")
    }
})
