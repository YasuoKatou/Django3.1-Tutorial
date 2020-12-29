$(function(){
    $('textarea.blog-content-view').autoExpand();
});

$('#addMyBlog').on("click", function() {
    //alert("addMyBlog click!");
    $("#myblog-edit-dialog").dialog({
        modal:true,
        title:"ブログ新規登録",
        width: "50vw"
    });
});