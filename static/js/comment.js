$(document).ready(function () {
    $('.reply-link').click(function (event) {
        event.preventDefault();
        var commentId = $(this).data('comment-id');
        $('#reply-to-id').val(commentId);
    });
});
