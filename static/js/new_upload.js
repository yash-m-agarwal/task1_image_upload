//function to get csrf_token bt cookie
function getCookie(name)
{
    let cookieValue = null;
    if (document.cookie && document.cookie !== '')
    {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

    let frm = $('#submit_image');

    let formData = new FormData();

    $('.butn').click(function () {
       $('#id_image').click();
    });

    $('#id_image').on('input', function () {
        let ins = document.getElementById('id_image').files.length;
        for (let x = 0; x < ins; x++) {
            formData.append("images[]", document.getElementById('id_image').files[x]);
        }
        $("#gallery tbody").prepend(
          "<tr><td>" + document.getElementById('id_image').files[0].name + "</td></tr>"
        );
        console.log($(this)[0].files[0]);
    });

    frm.submit( function() {

        let csrftoken = getCookie('csrftoken');
        let title = $('#id_title').val();
        let description = $('#id_description').val();

        formData.append('title',title);
        formData.append('description',description);
        formData.append('csrfmiddlewaretoken', csrftoken);

        alert("Images uploaded Successfully");

        $.ajax({
            type: 'post',
            url: '/image/new/',
            contentType: false,
            processData:false,
            data: formData,
            success: function (data) {
                alert(data);
            },
            error: function (err) {
                alert("Something went wrong!!" + err);
            }
        });
    });
