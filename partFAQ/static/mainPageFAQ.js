$(document).ready(() => {

    // Mengirim request GET
    $.getJSON("get_faq_content/", (data) => {

        $.each(data, (key, value) => {
            append_element = 
            // "<div class='card'>"+
            //     "<div class='card-header' id='heading" + value.pk + "'>"+
            //         "<h5 class='mb-0'>"+
            //             "<button class='btn btn-link' type='button' data-toggle='collapse' data-target='#collapse" + value.pk + "' aria-expanded='true' aria-controls='collapse" + value.pk + "'>" + 
            //                 value.question + 
            //             "</button>"+
            //         "</h5>"+
            //     "</div>"+
            //     "<div id='collapse" + value.pk + "' class='collapse' aria-labelledby='heading" + value.pk + "' data-parent='#accordion'>"+
            //         "<div class='card-body'>" + 
            //         value.answer + 
            //         "</div>"+
            //     "</div>"+
            // "</div>"
            "<h4><a href=\""+value.pk+"\">"+value.fields.question+"</a></h4>";

            $("#show_question").append(append_element);
        });
    });

    $("#submit_search").click(() => {
        if ($("#search_bar").val() != "") {
            $("#show_question").empty();

            search_input = $("#search_bar").val();
            csrftoken = Cookies.get('csrftoken');

            data_send = {
                'search': search_input,
                'csrfmiddlewaretoken': csrftoken
            }

            $.post('search/', data_send, (data) => {
                $.each(data, (key, value) => {
                    append_element = 
                    "<h4><a href=\""+value.pk+"\">"+value.fields.question+"</a></h4>";

                    $("#show_question").append(append_element);
                });
            });
        }
    })

    
});
          
