
$((function(context) {
    return function(){
        var containers = $('.product-container');
        containers.each(function(i, container) {
            console.log(containers)
            var pid = $(container).attr('data-product-id');
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            }).done(function(data) {
                $(container).html(data);
                // console.log(data)
            });
        });
    }
})(DMP_CONTEXT.get()));