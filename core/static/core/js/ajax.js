$(document).ready(function() {
    $('#add-button').click(function(e){
        console.log(cart_add_url)
        e.preventDefault(); // Prevent the default behaviour of the click
        $.ajax({
            type:'POST',
            url: cart_add_url,
            data: {
                product_id : $('#add-button').val(),
                product_quantity: $('#select option:selected').text(),
                csrfmiddlewaretoken: csrf_token,
                action: 'post'
            },
            success: function(data){
                //Handle the ajax response
                console.log(data)

            },
            error: function(xhr, status, error){
                //Handle the ajax error

            }

        })

    })
})