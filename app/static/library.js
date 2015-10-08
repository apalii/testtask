$(function() {
    $('body').on('change', '#search', function() {
        var url = '/search/' + this.value;
        window.location = url;
    });
    
    $('body').on('submit', '#searchForm', function(e) {
        e.preventDefault();    
    });
})