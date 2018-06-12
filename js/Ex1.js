$(document).ready(function () {
    $('#refresh').on('click', function() {
        display_News();
        display_Cookie();
    });
});

display_Cookie = function () {
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/cookie",
        success: function (cookie) {
                $('#cookie').empty()
                var div = $('<div/>');
                div.text(cookie)
                $('#cookie').append(div);

        },
        error: function (cookie) {
            console.log("error");
        },
    });
}

display_News = function () {
    $.ajax({
        type: "GET",
        dataType: "JSON",
        url: "http://localhost:7000/Ex1",
        success: function (new_list) {
            for (var i = 0; i < new_list.length; i++) {
                var new_title = $('<a/>');
                console.log( new_list[i]["link"])
                new_title.attr("href", new_list[i]["link"])
                new_title.text(new_list[i]["title"])
                $('body').append(new_title);
            }
        },
        error: function (feed) {
            console.log("error");
        },
    });
}






