def difine_styles():
    default_stylesheet = [
        {
            "selector": 'node',
            'style': {
                "opacity": 1,
                'z-index': 9999
            }
        },
        {
            "selector": 'edge',
            'style': {
                "curve-style": "bezier",
                "opacity": 0.15,
                'z-index': 5000
            }
        },
        {
            'selector': '.followerNode',
            'style': {
                'background-color': '$primary'
            }
        },
        {
            'selector': '.followerEdge',
            "style": {
                "mid-target-arrow-color": "blue",
                "mid-target-arrow-shape": "vee",
                "line-color": "#0074D9"
            }
        },
        {
            'selector': '.followingNode',
            'style': {
                'background-color': '#FF4136'
            }
        },
        {
            'selector': '.followingEdge',
            "style": {
                "mid-target-arrow-color": "red",
                "mid-target-arrow-shape": "vee",
                "line-color": "#FF4136",
            }
        },
        {
            "selector": '.genesis',
            "style": {
                'background-color': '#B10DC9',
                "border-width": 2,
                "border-color": "purple",
                "border-opacity": 1,
                "opacity": 1,

                "label": "data(label)",
                "color": "#B10DC9",
                "text-opacity": 1,
                "font-size": 12,
                'z-index': 9999
            }
        },
        {
            'selector': ':selected',
            "style": {
                "border-width": 2,
                "border-color": "black",
                "border-opacity": 1,
                "opacity": 1,
                "label": "data(label)",
                "color": "black",
                "font-size": 12,
                'z-index': 9999
            }
        }
    ]
    return default_stylesheet
