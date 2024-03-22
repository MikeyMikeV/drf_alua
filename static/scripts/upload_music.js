(
    function ($){
        $('form').submit(function (event){
            event.preventDefault();

            var data = new FormData(this)

            var action = function (d){
                console.log(data.file_field)
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/rest/upload_music/',
                enctype: "multipart/form-data",
                data: data,
                type: 'POST',
                contentType: false,
                processData: false,
                success: action,
                error: action
            })
        })
    }
(jQuery))