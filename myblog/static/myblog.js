/**
 * 初期処理
 */
$(function(){
  // 投稿本文のテキストエリアの高さを自動調整する
  $('textarea.blog-content-view').autoExpand();
});

/**
 * ブログの新規登録を行う
 */
$('#addMyBlog').on("click", function() {
  // 入力項目の初期化
  $('#myblog-new-dialog input[name="content_title"]').val("")
  $("#myblog-new-dialog textarea").val("")
  // 入力フォーム（ダイアログ）の表示
  $("#myblog-new-dialog").dialog({
    modal:true,
    title:"ブログ新規登録",
    width: "50vw"
  });
});

// csrf_tokenの取得に使う
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// 投稿のタイトルをクリックで、投稿内容を変更する
$('h1.blog-item-header-title').on("click", function() {
  var blogId = $(this).parent().find(".blog-item-header-id")[0];
  // alert("title clicked (id:" + blogId.textContent + ")");
  // $.post( location.host + '/myblog/get_blog_by_id', 'id=' + blogId.textContent );
  var csrf_token = getCookie("csrftoken");
  $.ajax({
    type: "POST",
    url: "/myblog/get_blog_by_id/",
    contentType: "application/json",
    data: {"myblog_id": blogId.textContent},
    timeout: 5000,
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
    }
  }).done(function(data) {
    // alert("ajax success !!")
    showBlogEditor(data);
  }).fail(function() {
    alert("ajax fail !!")
  });
});

/**
 * ブログの編集を行う
 */
function showBlogEditor(data) {
  // 入力項目の初期化
  $('#myblog-edit-dialog input[name="myblog-id"]').val(data.myblog_id)
  $('#myblog-edit-dialog input[name="content_title"]').val(data.content_title)
  $('#myblog-edit-dialog textarea').val(data.content_text)
  // 編集フォーム（ダイアログ）の表示
  $("#myblog-edit-dialog").dialog({
    modal:true,
    title:"ブログ更新",
    width: "50vw"
  });
}

$("#editTag").on("click", function() {
  var csrf_token = getCookie("csrftoken");
  $.ajax({
    type: "POST",
    url: "/myblog/get_tag_list/",
    contentType: "application/json",
    data: {},
    timeout: 5000,
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
  }
  }).done(function(data) {
    // alert("editTag ajax success !!")
    showBlogTagList(data);
  }).fail(function() {
    alert("editTag ajax fail !!")
  });
});

function refreshTagList(data) {
  // 一覧のクリア
  $('#myblog-tag-list li').remove();
  // 一覧に追加
  data.list.forEach(function(item) {
    var tagName = '<p class="tag-list-name">' + item.name + "</p>"
    var tagId   = '<p class="tag-list-id" style="display:none;">' + item.id + "</p>"
    $('#myblog-tag-list ul').append("<li>" + tagName + tagId + "</li>");
  });
}

function showBlogTagList(data) {
  refreshTagList(data);
  // タグ一覧（ダイアログ）の表示
  $("#myblog-tag-list").dialog({
    modal:true,
    title:"タグ一覧",
    width: "20vw"
  });
}

$("#add-tag-list").on("click", function() {
  var csrf_token = getCookie("csrftoken");
  $.ajax({
    type: "POST",
    url: "/myblog/add_tag_list/",
    contentType: "application/json",
    data: {"tag_text": $("#add-tag-name").val()},
    timeout: 5000,
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
  }
  }).done(function(data) {
    // alert("addTag ajax success !!")
    refreshTagList(data);
  }).fail(function() {
    alert("addTag ajax fail !!")
  });
});
