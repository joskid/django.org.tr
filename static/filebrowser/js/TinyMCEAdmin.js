function CustomFileBrowser(field_name, url, type, win) {
    // alert("Field_Name: " + field_name + "\nURL: " + url + "\nType: " + type + "\nWin: " + win); // debug/testing
    var fileBrowserWindow = new Array();

    fileBrowserWindow['title'] = 'File Browser';
    fileBrowserWindow['file'] = "/admin/filebrowser/?pop=2";
    fileBrowserWindow['width'] = '820';
    fileBrowserWindow['height'] = '600';
    fileBrowserWindow['close_previous'] = 'no';
    tinyMCE.openWindow(fileBrowserWindow, {
      window : win,
      input : field_name,
      resizable : 'yes',
      scrollbars : 'yes',
      inline : 'yes',
      editorID: tinyMCE.getWindowArg('editor_id')
    });
    return false;
  }

function myCustomSetupContent(editor_id, body, doc) {
    if (body.innerHTML == "") {
        body.innerHTML = "<p>xxx</p>";
    }
}

tinyMCE.init({
  mode : "textareas",
  theme : "advanced",
  theme_advanced_toolbar_location : "top",
  theme_advanced_toolbar_align : "left",
  theme_advanced_buttons1 : "fullscreen,separator,preview,separator,bold,italic,underline,strikethrough,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,link,unlink,anchor,separator,image,cleanup,help,separator,code,template",
  theme_advanced_buttons2 : "",
  theme_advanced_buttons3 : "",
  plugins : "table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,zoom,flash,searchreplace,print,contextmenu,fullscreen,template",
  plugin_insertdate_dateFormat : "%d/%m/%Y",
  plugin_insertdate_timeFormat : "%H:%M:%S",
  fullscreen_new_window : true,
  fullscreen_settings : {
    theme_advanced_path_location : "top",
    theme_advanced_buttons1 : "fullscreen,separator,preview,separator,cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
    theme_advanced_buttons2 : "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor",
    theme_advanced_buttons3 : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print"
  },
  advimage_update_dimensions_onchange: true,
  file_browser_callback : "CustomFileBrowser",
  entity_encoding : "raw",
  relative_urls : false,
  valid_elements : "*[*]"
});
