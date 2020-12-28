$('#addMyBlog').on("click", function() {
    //alert("addMyBlog click!");
    $("#myblog-edit-dialog").dialog({
        modal:true,
        title:"ブログ新規登録",
        width: "50vw",
        buttons: {
            "追加": function() {
                // TODO
                $(this).dialog("close");
            },
            "キャンセル": function() {
                $(this).dialog("close");
            }
        }
    });
});