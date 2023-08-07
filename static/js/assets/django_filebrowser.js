function fileBrowserCallBack(field_name, url, type, win) {
    var filebrowserUrl = '/filebrowser/';
    filebrowserUrl += '?pop=3';
    filebrowserUrl += '&type=' + type;
    filebrowserUrl += '&input=' + field_name;
    tinyMCE.activeEditor.windowManager.open({
        title: 'FileBrowser',
        url: filebrowserUrl,
        width: 850,
        height: 500,
        resizable: 'yes',
        close_previous: 'no',
    }, {
        window: win,
        input: field_name,
    });
}