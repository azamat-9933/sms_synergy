customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_FILE_STORAGE = "consulting.custom_storage.CustomStorage"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough', 'subscript', 'superscript',
            'code', 'blockquote', 'codeBlock', 'highlight', '|', 'bulletedList', 'numberedList', 'todoList',
            'outdent', 'indent', '|', 'imageUpload', 'mediaEmbed', 'insertTable', '|', 'removeFormat',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|', 'alignment:left',
            'alignment:center', 'alignment:right', 'alignment:justify', '|', 'horizontalLine',
            'pageBreak', 'sourceEditing'
        ],
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 'imageStyle:inline', 'imageStyle:block', 'imageStyle:side',
                '|', 'imageStyle:alignLeft', 'imageStyle:alignRight', 'imageStyle:alignCenter'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter', 'inline', 'block'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells', 'tableProperties', 'tableCellProperties'
            ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6'}
            ]
        },
    }
}
