import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import json


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Letters For You",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# AUDIO HELPER
# =========================================================

def file_to_data_uri(path_str):
    path = Path(path_str)

    if not path.exists():
        return ""

    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:audio/mpeg;base64,{encoded}"


def image_asset_data_uri(path_without_extension):
    """
    Lets you upload .jpg, .jpeg, .png, or .webp images without
    changing the Python code's base filename.
    Example:
        assets/images/letter1/photo1.jpg
        assets/images/letter1/photo1.png
    Both can be referenced as:
        image_asset_data_uri("assets/images/letter1/photo1")
    """

    supported = [
        (".jpg", "image/jpeg"),
        (".jpeg", "image/jpeg"),
        (".png", "image/png"),
        (".webp", "image/webp"),
    ]

    for extension, mime_type in supported:
        path = Path(path_without_extension + extension)

        if path.exists():
            encoded = base64.b64encode(
                path.read_bytes()
            ).decode("utf-8")

            return (
                f"data:{mime_type};base64,"
                f"{encoded}"
            )

    return ""


# =========================================================
# LETTERS + MUSIC + OPTIONAL POLAROIDS / STAMPS
#
# start_time is in SECONDS.
#
# Examples:
# 0:42 = 42
# 1:17 = 77
# 2:05 = 125
# =========================================================

letter_data = {
    "1": {
        "text": '''When you lose sight of purpose, remember Melbourne.

Think of how alive you felt. How intriguing it was when we exited the airport
and it was as though the sky was an aircon. How cute it was when the villagers
waved at us on the Puffing Billy. How cool it was seeing cows, sheeps and
the 12 apostles at Great Ocean Road.

And Mr Summit's Flat White and Toasties? Wew, there will be so many more Mr Summits to discover!

There is so much more we have yet to experience. And I look forward to more firsts with you.

When the world comes to an end, I hope I get to say, "I had the time of my life fighting dragons with you!<3"''',
        "signature": "Love, R ♡",
        "song_title": "long live",
        "artist": "Taylor Swift ♡",
        "audio": file_to_data_uri("assets/music/letter1.mp3"),
        "start_time": 173,

        # OPTIONAL POLAROIDS
        # Upload these as .jpg, .jpeg, .png, or .webp.
        # If a file does not exist, it simply will not appear.
        "polaroids": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter1/photo1"
                ),
                "caption": "Melbourne ♡",

                # Position: negative x = left, positive x = right
                # negative y = up, positive y = down
                "x": -10,
                "y": 0,

                # Polaroid width + PHOTO height, in pixels
                "width": 220,
                "height": 200,

                # Negative = tilt left, positive = tilt right
                "rotation": -4,
            },
            {
                "image": image_asset_data_uri(
                    "assets/images/letter1/photo2"
                ),
                "caption": "another little memory",
                "x": 10,
                "y": -8,
                "width": 190,
                "height": 170,
                "rotation": 3,
            },
        ],

        # OPTIONAL STAMPS
        "stamps": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter1/stamp1"
                ),
                "x": -8,
                "y": 0,
                "width": 74,
                "height": 92,
                "rotation": 7,
            },
            {
                "image": image_asset_data_uri(
                    "assets/images/letter1/stamp2"
                ),
                "x": 8,
                "y": 8,
                "width": 74,
                "height": 92,
                "rotation": -5,
            },
        ],
    },

    "2": {
        "text": """Reminder:

You are kind, you are funny, you are generous.
You are gentle, you are honest, you are smart.

You are caring, and you are cared for.
You are loving, and you are loved.

You are God's creation and he creates nothing less than perfect.

You are beautiful, and you are more than enough.""",
        "signature": "Love, R ☺",
        "song_title": "who says",
        "artist": "Selena Gomez ♡",
        "audio": file_to_data_uri("assets/music/letter2.mp3"),
        "start_time": 47,

        "polaroids": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter2/photo1"
                ),
                "caption": "",
                "x": -10,
                "y": 0,
                "width": 190,
                "height": 170,
                "rotation": -3,
            },
            {
                "image": image_asset_data_uri(
                    "assets/images/letter2/photo2"
                ),
                "caption": "",
                "x": 10,
                "y": -10,
                "width": 190,
                "height": 170,
                "rotation": 3,
            },
        ],

        "stamps": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter2/stamp1"
                ),
                "x": 0,
                "y": 0,
                "width": 74,
                "height": 92,
                "rotation": 5,
            },
        ],
    },

    "3": {
        "text": """Dear N,

This is just a little reminder
that I am always cheering
for you.

Take your time.
Keep going.
And remember to be kind
to yourself too.""",
        "signature": "Love, R ☆",
        "song_title": "song three",
        "artist": "Your Artist Name ♡",
        "audio": file_to_data_uri("assets/music/letter3.mp3"),
        "start_time": 125,

        "polaroids": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter3/photo1"
                ),
                "caption": "",
                "x": 0,
                "y": 0,
                "width": 190,
                "height": 170,
                "rotation": 4,
            },
        ],

        "stamps": [
            {
                "image": image_asset_data_uri(
                    "assets/images/letter3/stamp1"
                ),
                "x": 0,
                "y": 0,
                "width": 74,
                "height": 92,
                "rotation": -6,
            },
        ],
    },
}

letters_json = json.dumps(letter_data)


# =========================================================
# HIDE NORMAL STREAMLIT UI
# =========================================================

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .stApp {
            background:
                radial-gradient(circle at 12% 15%, rgba(83,41,83,.23), transparent 25%),
                radial-gradient(circle at 80% 45%, rgba(47,25,63,.22), transparent 35%),
                #090711;
        }

        .block-container {
            padding: 0 !important;
            max-width: none !important;
        }

        iframe {
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# WEBSITE
#
# IMPORTANT:
# This is NOT an f-string. CSS and JavaScript contain lots
# of { } braces. We insert the JSON later using .replace().
# =========================================================

html = r"""
<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    background: #090711;
}

body {
    overflow: visible;
}

#letter-app {
    min-height: 1080px;
    color: #f9e8ee;
    overflow: hidden;

    background:
        radial-gradient(circle at 8% 15%, rgba(255,255,255,.50) 0 1px, transparent 1.5px),
        radial-gradient(circle at 73% 11%, rgba(247,150,196,.45) 0 1px, transparent 1.4px),
        radial-gradient(circle at 92% 31%, rgba(255,255,255,.35) 0 1px, transparent 1.5px),
        radial-gradient(circle at 11% 78%, rgba(235,139,191,.35) 0 1px, transparent 1.4px),
        radial-gradient(circle at 45% 44%, rgba(237,143,193,.25), transparent 35%),
        linear-gradient(135deg, #080610 0%, #0d0813 48%, #090710 100%);
}


/* ========================================================
   MAIN LAYOUT
======================================================== */

.page {
    width: min(1390px, calc(100% - 50px));
    margin: 0 auto;

    display: grid;
    grid-template-columns: 500px minmax(0, 1fr);
    column-gap: 45px;

    padding-top: 24px;
    padding-bottom: 40px;
}

.left-column {
    min-width: 0;
}

.right-column {
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 18px;
}

/*
Left = 158 intro + 812 envelope window = 970px
Right = 767 letter + 18 gap + 185 music = 970px
*/
@media (min-width: 1051px) {
    .right-column {
        height: 970px;
        display: grid;
        grid-template-rows: minmax(0, 1fr) 185px;
        gap: 18px;
    }
}


/* ========================================================
   INTRO
======================================================== */

.intro {
    min-height: 158px;
    padding-left: 5px;
}

.title {
    margin: 0;
    color: #ef9abb;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        "Comic Sans MS",
        cursive;

    font-size: 49px;
    font-weight: 400;
    line-height: 1;
    letter-spacing: 1px;
}

.title-heart {
    display: inline-block;
    margin-left: 8px;
    font-size: 47px;
    transform: rotate(-4deg);
}

.subtitle {
    margin-top: 22px;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        "Comic Sans MS",
        cursive;

    font-size: 18px;
    line-height: 1.8;
    color: #f5d9cc;
}

.subtitle-heart {
    color: #ee8fb6;
}


/* ========================================================
   FAKE WINDOWS
======================================================== */

.window {
    position: relative;

    border: 1.25px solid rgba(239,135,181,.9);
    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(16,11,23,.92),
            rgba(11,8,17,.96)
        );

    overflow: hidden;

    box-shadow:
        0 14px 40px rgba(0,0,0,.20),
        inset 0 0 30px rgba(238,136,182,.015);
}

.window-bar {
    height: 46px;

    display: flex;
    justify-content: flex-end;
    align-items: center;

    padding: 0 17px;
    gap: 15px;

    border-bottom: 1px solid rgba(239,135,181,.67);
}

.window-control {
    color: #ee91b7;
    font-family: Arial, sans-serif;
    font-size: 20px;
    font-weight: 300;
    line-height: 1;
}

.fake-square {
    width: 15px;
    height: 15px;
    border: 2px solid #ee91b7;
    display: inline-block;
}


/* ========================================================
   DECORATIONS
======================================================== */

.sparkle {
    position: absolute;
    color: #ed91b8;
    font-family: Georgia, serif;
    opacity: .9;
    pointer-events: none;
}

.sparkle.one {
    left: 25px;
    top: 205px;
    font-size: 24px;
}

.sparkle.two {
    right: 13px;
    top: 330px;
    font-size: 22px;
}

.sparkle.three {
    right: 25px;
    top: 680px;
    font-size: 27px;
}

.paper-plane {
    position: absolute;
    left: 6px;
    top: 290px;
    color: #df7fa9;
    font-size: 34px;
    transform: rotate(-22deg);
    opacity: .75;
}


/* ========================================================
   ENVELOPE WINDOW
======================================================== */

.envelope-window {
    min-height: 812px;
    height: 812px;
}

.envelope-list {
    height: calc(100% - 46px);

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

    padding: 24px 25px 28px;
}


/* ========================================================
   ENVELOPE + HOVER LETTER
======================================================== */

.envelope-item {
    position: relative;
    width: 304px;
    height: 206px;

    cursor: pointer;
    isolation: isolate;
    outline: none;
}

.peek {
    position: absolute;
    z-index: 0;

    left: 52px;
    bottom: 25px;

    width: 200px;
    height: 145px;
    padding: 22px;

    background:
        repeating-linear-gradient(
            0deg,
            rgba(126,76,55,.04) 0,
            rgba(126,76,55,.04) 1px,
            transparent 1px,
            transparent 26px
        ),
        #f5dec2;

    color: #292027;

    font-family: "Courier New", monospace;
    font-size: 13px;
    line-height: 1.55;

    border-radius: 2px;
    box-shadow: 0 12px 24px rgba(0,0,0,.28);

    opacity: 0;
    transform: translateY(28px) rotate(-1deg);

    transition:
        transform .55s cubic-bezier(.17,.78,.27,1),
        opacity .25s ease;
}

.envelope-item:hover .peek,
.envelope-item:focus .peek {
    opacity: 1;
    transform: translateY(-84px) rotate(-1deg);
}

.envelope-object {
    position: absolute;
    z-index: 2;

    left: 0;
    bottom: 0;

    width: 304px;
    height: 198px;

    border-radius: 7px;
    overflow: hidden;

    box-shadow: 0 16px 30px rgba(0,0,0,.33);

    transition:
        transform .32s ease,
        filter .32s ease,
        box-shadow .32s ease;
}

.envelope-item:hover .envelope-object {
    transform: translateY(5px) scale(1.015);
    filter: brightness(1.035);

    box-shadow:
        0 20px 34px rgba(0,0,0,.36),
        0 0 22px rgba(234,134,179,.10);
}

.env-background {
    position: absolute;
    inset: 0;
}

.env-background::after {
    content: "";
    position: absolute;
    inset: 0;

    opacity: .17;

    background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,.9) 0 1px, transparent 1.5px),
        radial-gradient(circle at 73% 58%, rgba(63,22,45,.35) 0 1px, transparent 1.5px);

    background-size:
        25px 27px,
        31px 34px;
}

.env-pink .env-background {
    background:
        linear-gradient(
            145deg,
            #ff91b0 0%,
            #ef7fa6 42%,
            #d86e99 100%
        );
}

.env-cream .env-background {
    background:
        linear-gradient(
            145deg,
            #ffe1b1 0%,
            #f4c98e 45%,
            #e8b876 100%
        );
}

.env-lilac .env-background {
    background:
        linear-gradient(
            145deg,
            #d99ee4 0%,
            #c27ed3 45%,
            #9e65b8 100%
        );
}


/* ========================================================
   ENVELOPE FOLDS
======================================================== */

.env-left-fold,
.env-right-fold,
.env-bottom-fold,
.env-flap {
    position: absolute;
}

.env-left-fold {
    z-index: 3;
    left: 0;
    bottom: 0;

    width: 61%;
    height: 75%;

    clip-path:
        polygon(
            0 0,
            100% 100%,
            0 100%
        );

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.14),
            rgba(0,0,0,.03)
        );

    border-right: 1px solid rgba(90,49,76,.23);
}

.env-right-fold {
    z-index: 3;
    right: 0;
    bottom: 0;

    width: 61%;
    height: 75%;

    clip-path:
        polygon(
            100% 0,
            100% 100%,
            0 100%
        );

    background:
        linear-gradient(
            225deg,
            rgba(255,255,255,.11),
            rgba(0,0,0,.035)
        );

    border-left: 1px solid rgba(90,49,76,.20);
}

.env-bottom-fold {
    z-index: 4;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 66%;

    clip-path:
        polygon(
            0 100%,
            50% 28%,
            100% 100%
        );

    background:
        linear-gradient(
            to top,
            rgba(255,255,255,.10),
            rgba(255,255,255,.025)
        );
}

.env-flap {
    z-index: 5;

    top: 0;
    left: 0;

    width: 100%;
    height: 69%;

    clip-path:
        polygon(
            0 0,
            100% 0,
            50% 94%
        );

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.18),
            rgba(255,255,255,.025)
        );

    filter: drop-shadow(0 5px 3px rgba(64,29,48,.20));
}

.env-flap::after {
    content: "";
    position: absolute;
    inset: 0;

    clip-path:
        polygon(
            0 0,
            100% 0,
            50% 94%
        );

    border-bottom: 2px solid rgba(71,37,62,.25);
}


/* ========================================================
   ENVELOPE SYMBOLS
======================================================== */

.env-symbol {
    position: absolute;
    z-index: 9;

    right: 22px;
    bottom: 21px;

    color: #332238;

    font-family:
        "Segoe Print",
        "Comic Sans MS",
        cursive;
}

.heart-symbol {
    font-size: 45px;
    line-height: .7;
}

.smile-symbol {
    font-size: 38px;
}

.star-symbol {
    width: 59px;
    height: 50px;

    position: absolute;
    z-index: 9;

    right: 17px;
    bottom: 17px;
}

.star-symbol span {
    position: absolute;
    color: #352239;
    font-size: 37px;
    line-height: 1;
}

.star-symbol span:first-child {
    left: 0;
    top: 0;
}

.star-symbol span:last-child {
    right: 0;
    bottom: -4px;
    font-size: 31px;
}


/* ========================================================
   FULL LETTER WINDOW
======================================================== */

.full-window {
    height: 590px;
}

@media (min-width: 1051px) {
    .full-window {
        height: 100%;
    }
}

.full-inside {
    height: calc(100% - 46px);
    min-height: 0;
    padding: 18px 31px;
    overflow: hidden;
}

/* ========================================================
   SCROLL ONLY THE FULL LETTER
======================================================== */

.paper-scroll {
    width: 88%;
    max-width: 650px;
    height: 100%;
    min-height: 0;
    margin: 0 auto;

    overflow-y: scroll;
    overflow-x: hidden;

    padding-right: 10px;

    /* Make the letter independently scrollable on touch devices. */
    -webkit-overflow-scrolling: touch;
    overscroll-behavior: contain;
    touch-action: pan-y;

    scrollbar-gutter: stable both-edges;
    scrollbar-width: thin;
    scrollbar-color: #df83aa rgba(95, 55, 78, .16);
}

.paper-scroll::-webkit-scrollbar {
    width: 9px;
}

.paper-scroll::-webkit-scrollbar-track {
    background: rgba(95, 55, 78, .10);
    border-radius: 999px;
}

.paper-scroll::-webkit-scrollbar-thumb {
    background: #df83aa;
    border-radius: 999px;
}

.paper-scroll::-webkit-scrollbar-thumb:hover {
    background: #ee9abb;
}


/* ========================================================
   LETTER PAPER
======================================================== */

.paper {
    position: relative;

    width: 100%;
    max-width: none;

    min-height: 100%;
    height: auto;

    margin: 0;

    overflow: visible;

    padding:
        48px
        62px
        42px;

    color: #241d1c;

    background:
        radial-gradient(circle at 13% 22%, rgba(126,83,45,.05) 0 1px, transparent 1.5px),
        radial-gradient(circle at 69% 70%, rgba(126,83,45,.045) 0 1px, transparent 1.5px),
        linear-gradient(
            100deg,
            rgba(172,107,60,.045),
            transparent 23%,
            rgba(255,255,255,.13) 50%,
            transparent 70%
        ),
        #f4d8b6;

    background-size:
        26px 27px,
        31px 33px,
        auto,
        auto;

    clip-path:
        polygon(
            0.5% 4%,
            4% 1.5%,
            9% 2%,
            14% .7%,
            19% 1.5%,
            24% .6%,
            30% 1.5%,
            36% .5%,
            42% 1.3%,
            49% .5%,
            55% 1.3%,
            62% .5%,
            69% 1.5%,
            76% .7%,
            83% 1.6%,
            90% .6%,
            97% 2%,
            99.5% 5%,

            99% 13%,
            100% 21%,
            99.2% 29%,
            100% 37%,
            99% 47%,
            100% 56%,
            99% 66%,
            100% 75%,
            99% 85%,
            99.7% 95%,

            96% 99%,
            89% 98.5%,
            82% 100%,
            74% 98.8%,
            67% 100%,
            59% 98.7%,
            51% 100%,
            43% 98.8%,
            35% 100%,
            27% 98.8%,
            19% 100%,
            11% 98.8%,
            4% 99.5%,
            .5% 96%,

            1% 87%,
            0% 77%,
            1% 68%,
            0% 59%,
            1% 49%,
            0% 40%,
            1% 31%,
            0% 21%,
            1% 12%
        );

    filter:
        drop-shadow(
            0 13px 15px rgba(0,0,0,.29)
        );

    transition:
        opacity .25s ease,
        transform .25s ease;
}


.paper.paper-changing {
    opacity: 0;
    transform: translateY(7px) scale(.99);
}

.letter-text {
    white-space: pre-line;

    font-family:
        "Courier New",
        monospace;

    font-size: 18px;
    line-height: 1.65;
    letter-spacing: .1px;
}


/* ========================================================
   OPTIONAL POLAROIDS INSIDE THE LETTER
======================================================== */

.letter-polaroids {
    display: none;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;

    gap: 24px 18px;

    margin:
        34px
        0
        30px;
}

.letter-polaroids.has-items {
    display: flex;
}

.polaroid {
    flex: 0 0 auto;

    /*
    width is controlled per photo in letter_data.
    It is capped so it cannot break the letter on small screens.
    */
    width:
        min(
            var(--polaroid-width, 190px),
            calc(100% - 12px)
        );

    padding:
        10px
        10px
        28px;

    background:
        linear-gradient(
            145deg,
            #fffaf0,
            #f5eadc
        );

    border:
        1px solid
        rgba(91, 63, 54, .12);

    border-radius: 2px;

    box-shadow:
        0 10px 19px
        rgba(58, 36, 31, .20);

    /*
    x: negative = left, positive = right
    y: negative = up, positive = down
    */
    transform:
        translate(
            var(--polaroid-x, 0px),
            var(--polaroid-y, 0px)
        )
        rotate(
            var(--polaroid-rotation, 0deg)
        );

    transform-origin: center;

    transition:
        transform .2s ease;
}

.polaroid:hover {
    transform:
        translate(
            var(--polaroid-x, 0px),
            var(--polaroid-y, 0px)
        )
        rotate(0deg)
        scale(1.025);
}

.polaroid img {
    display: block;

    width: 100%;

    /*
    height is controlled per photo in letter_data.
    */
    height:
        var(--polaroid-height, 170px);

    object-fit: cover;

    background: #e9ddce;

    border:
        1px solid
        rgba(70, 48, 43, .12);

    filter:
        saturate(.92)
        contrast(.96);
}

.polaroid-caption {
    min-height: 16px;

    margin-top: 10px;

    padding:
        0
        3px;

    color: #4b3538;

    text-align: center;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        "Comic Sans MS",
        cursive;

    font-size: 13px;

    line-height: 1.35;
}


/* ========================================================
   OPTIONAL STAMPS INSIDE THE LETTER
======================================================== */

.letter-stamps {
    display: none;

    flex-wrap: wrap;
    justify-content: flex-end;
    align-items: center;

    gap: 9px;

    margin:
        4px
        4px
        28px;
}

.letter-stamps.has-items {
    display: flex;
}

.stamp {
    flex: 0 0 auto;

    width:
        min(
            var(--stamp-width, 74px),
            calc(100% - 8px)
        );

    height:
        var(--stamp-height, 92px);

    padding: 6px;

    background: #f8ead8;

    border:
        2px dashed
        rgba(95, 61, 70, .36);

    box-shadow:
        0 6px 12px
        rgba(64, 38, 39, .14);

    transform:
        translate(
            var(--stamp-x, 0px),
            var(--stamp-y, 0px)
        )
        rotate(
            var(--stamp-rotation, 0deg)
        );

    transform-origin: center;
}

.stamp img {
    display: block;

    width: 100%;
    height: 100%;

    object-fit: cover;

    border:
        1px solid
        rgba(78, 54, 55, .14);

    filter:
        saturate(.9)
        contrast(.96);
}



.signature {
    margin-top: 25px;

    font-family:
        "Courier New",
        monospace;

    font-size: 18px;
}

.paper-sparkle {
    position: absolute;

    right: 25px;
    top: 45px;

    color: #dc7fa5;
    font-size: 31px;
}


/* ========================================================
   MUSIC WINDOW
======================================================== */

.player-window {
    height: 185px;
}

.player-inside {
    height: calc(100% - 46px);

    padding: 18px 22px;

    display: flex;
    align-items: center;
}

.player {
    width: 100%;
    height: 100px;

    padding: 13px 18px;

    border: 1.25px solid rgba(239,135,181,.9);
    border-radius: 16px;

    background: rgba(11,8,18,.91);

    display: grid;

    grid-template-columns:
        205px
        1fr
        100px;

    align-items: center;
    column-gap: 16px;
}

.track-info {
    display: grid;

    grid-template-columns:
        35px
        1fr;

    gap: 8px;
    align-items: start;
}

.music-note {
    color: #f18fb8;
    font-size: 31px;
    line-height: 1;
}

.song-title {
    color: #f5c4d7;

    font-family:
        "Segoe Print",
        "Comic Sans MS",
        cursive;

    font-size: 17px;
}

.artist {
    margin-top: 5px;
    color: #e88cad;

    font-family:
        "Segoe Print",
        "Comic Sans MS",
        cursive;

    font-size: 13px;
}


/* ========================================================
   MUSIC CONTROLS
======================================================== */

.controls-section {
    min-width: 0;
}

.main-controls {
    height: 50px;

    display: flex;
    justify-content: center;
    align-items: center;

    gap: 31px;
}

.control-button {
    appearance: none;
    border: 0;
    background: transparent;

    color: #ef91b7;
    cursor: pointer;

    padding: 4px;

    font-size: 24px;
    font-family: Arial, sans-serif;
}

.play-button {
    width: 52px;
    height: 52px;

    border-radius: 50%;

    background: #f178a8;
    color: #1d111d;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 24px;
    padding-left: 7px;

    transition:
        transform .18s ease,
        filter .18s ease;
}

.play-button:hover {
    transform: scale(1.06);
    filter: brightness(1.06);
}

.progress-row {
    display: grid;

    grid-template-columns:
        40px
        minmax(0, 1fr)
        42px;

    gap: 10px;
    align-items: center;

    color: #f0c5d4;

    font-family:
        "Courier New",
        monospace;

    font-size: 12px;
}

.progress-track {
    position: relative;

    height: 4px;
    border-radius: 999px;

    background: #564052;
    cursor: pointer;
}

.progress-fill {
    position: relative;

    width: 0%;
    height: 100%;

    border-radius: inherit;
    background: #eb8eb5;
}

.progress-dot {
    position: absolute;

    right: -5px;
    top: -3px;

    width: 10px;
    height: 10px;

    border-radius: 50%;
    background: #e98bb3;
}

.right-controls {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    gap: 7px;

    color: #e68cb0;
    font-size: 23px;
}

.volume {
    font-size: 22px;
}

.player-heart {
    font-family: Arial, sans-serif;
    font-size: 28px;
}


/* ========================================================
   TABLET
======================================================== */

@media (max-width: 1050px) {

    #letter-app {
        min-height: 1550px;
    }

    .page {
        width: min(760px, calc(100% - 28px));
        grid-template-columns: 1fr;
        gap: 18px;
        padding-top: 22px;
    }

    .right-column {
        height: auto;
        display: flex;
        flex-direction: column;
        gap: 18px;
    }

    .envelope-window {
        height: 660px;
        min-height: 660px;
    }

    .envelope-list {
        min-height: 612px;
        height: calc(100% - 46px);

        flex-direction: row;
        flex-wrap: wrap;
        align-content: space-around;

        gap: 15px;
    }

    .envelope-item {
        transform: scale(.82);
        margin: -15px -20px;
    }

    .full-window {
        height: 625px;
    }

    .paper-scroll {
        width: 90%;
    }
}


/* ========================================================
   PHONE
======================================================== */

@media (max-width: 650px) {

    #letter-app {
        min-height: 1900px;
        height: auto;
        overflow: visible;
    }

    .page {
        width: calc(100% - 18px);
        padding-top: 12px;
    }

    .intro {
        min-height: 140px;
    }

    .title {
        font-size: 37px;
    }

    .title-heart {
        font-size: 37px;
    }

    .subtitle {
        font-size: 14px;
    }

    .envelope-window {
        height: 810px;
        min-height: 810px;
    }

    .envelope-list {
        flex-direction: column;
        flex-wrap: nowrap;
        min-height: 760px;
    }

    .envelope-item {
        transform: scale(.86);
        margin: 0;
    }

    .full-window {
        height: 610px;
        min-height: 610px;
    }

    .full-inside {
        height: calc(100% - 46px);
        min-height: 0;
        padding: 12px 8px 14px;
        overflow: hidden;
    }

    .paper-scroll {
        width: 100%;
        max-width: none;
        height: 100%;
        min-height: 0;
        padding-right: 6px;

        overflow-y: auto;
        overflow-x: hidden;

        -webkit-overflow-scrolling: touch;
        overscroll-behavior: contain;
        touch-action: pan-y;
    }

    .paper {
        width: 100%;
        min-height: 100%;
        height: auto;

        padding:
            38px
            26px
            36px;
    }

    .letter-text {
        font-size: 15px;
        line-height: 1.7;
        overflow-wrap: anywhere;
    }

    .letter-polaroids {
        gap: 20px 12px;
        margin: 28px 0 25px;
    }

    .polaroid {
        width:
            min(
                var(--polaroid-width, 155px),
                calc(100% - 12px)
            );

        padding:
            8px
            8px
            23px;
    }

    .polaroid img {
        height:
            var(--polaroid-height, 150px);
    }

    .polaroid-caption {
        font-size: 11px;
    }

    .letter-stamps {
        gap: 7px;
        margin-bottom: 22px;
    }

    .stamp {
        width:
            min(
                var(--stamp-width, 58px),
                calc(100% - 8px)
            );

        height:
            var(--stamp-height, 72px);

        padding: 5px;
    }

    .signature {
        font-size: 15px;
        overflow-wrap: anywhere;
    }

    .paper-sparkle {
        display: none;
    }

    .player-window {
        height: auto;
    }

    .player-inside {
        height: auto;
    }

    .player {
        width: 100%;
        height: auto;
        min-height: 165px;

        grid-template-columns: 1fr;
        gap: 10px;
    }

    .track-info {
        width: 180px;
        margin: auto;
    }

    .right-controls {
        justify-content: center;
    }
}

@media (max-width: 390px) {

    .title {
        font-size: 32px;
    }

    .subtitle {
        font-size: 13px;
    }

    .envelope-item {
        transform: scale(.78);
    }

    .full-window {
        height: 570px;
        min-height: 570px;
    }

    .paper {
        padding:
            34px
            21px
            32px;
    }

    .letter-text,
    .signature {
        font-size: 14px;
    }
}

</style>


<div id="letter-app">

    <div class="sparkle one">✧</div>
    <div class="sparkle two">⋆</div>
    <div class="sparkle three">✦</div>
    <div class="paper-plane">➤</div>


    <main class="page">

        <!-- LEFT COLUMN -->

        <section class="left-column">

            <header class="intro">

                <h1 class="title">
                    Letters For You
                    <span class="title-heart">♡</span>
                </h1>

                <div class="subtitle">
                    Some things are better written than said.
                    <br>
                    Choose an envelope whenever you're ready.
                    <span class="subtitle-heart">♥</span>
                </div>

            </header>


            <!-- ENVELOPES -->

            <section class="window envelope-window">

                <div class="window-bar">
                    <span class="window-control">−</span>
                    <span class="fake-square"></span>
                    <span class="window-control">×</span>
                </div>


                <div class="envelope-list">

                    <!-- LETTER 1 -->

                    <div
                        class="envelope-item"
                        tabindex="0"
                        data-letter="1"
                    >

                        <div class="peek">
                            Dear N,
                            <br><br>
                            You did great today &amp;
                            it is all going to...
                        </div>

                        <div class="envelope-object env-pink">

                            <div class="env-background"></div>
                            <div class="env-left-fold"></div>
                            <div class="env-right-fold"></div>
                            <div class="env-bottom-fold"></div>
                            <div class="env-flap"></div>

                            <div class="env-symbol heart-symbol">
                                ♡
                            </div>

                        </div>

                    </div>


                    <!-- LETTER 2 -->

                    <div
                        class="envelope-item"
                        tabindex="0"
                        data-letter="2"
                    >

                        <div class="peek">
                            Dear N,
                            <br><br>
                            I hope you know just how
                            special you are...
                        </div>

                        <div class="envelope-object env-cream">

                            <div class="env-background"></div>
                            <div class="env-left-fold"></div>
                            <div class="env-right-fold"></div>
                            <div class="env-bottom-fold"></div>
                            <div class="env-flap"></div>

                            <div class="env-symbol smile-symbol">
                                ☺
                            </div>

                        </div>

                    </div>


                    <!-- LETTER 3 -->

                    <div
                        class="envelope-item"
                        tabindex="0"
                        data-letter="3"
                    >

                        <div class="peek">
                            Dear N,
                            <br><br>
                            This is just a little
                            reminder...
                        </div>

                        <div class="envelope-object env-lilac">

                            <div class="env-background"></div>
                            <div class="env-left-fold"></div>
                            <div class="env-right-fold"></div>
                            <div class="env-bottom-fold"></div>
                            <div class="env-flap"></div>

                            <div class="star-symbol">
                                <span>☆</span>
                                <span>☆</span>
                            </div>

                        </div>

                    </div>

                </div>

            </section>

        </section>


        <!-- RIGHT COLUMN -->

        <section class="right-column">


            <!-- FULL LETTER -->

            <section class="window full-window">

                <div class="window-bar">
                    <span class="window-control">−</span>
                    <span class="fake-square"></span>
                    <span class="window-control">×</span>
                </div>


                <div class="full-inside">

                    <div
                        class="paper-scroll"
                        id="paperScroll"
                    >

                        <article
                            class="paper"
                            id="paper"
                        >

                            <div
                                class="letter-text"
                                id="letterText"
                            ></div>

                            <div
                                class="letter-polaroids"
                                id="letterPolaroids"
                                aria-label="Letter photos"
                            ></div>

                            <div
                                class="letter-stamps"
                                id="letterStamps"
                                aria-label="Letter stamps"
                            ></div>

                            <div
                                class="signature"
                                id="signature"
                            ></div>

                            <div class="paper-sparkle">
                                ✧
                                <br>
                                ✦
                            </div>

                        </article>

                    </div>

                </div>

            </section>


            <!-- MUSIC PLAYER -->

            <section class="window player-window">

                <div class="window-bar">
                    <span class="window-control">−</span>
                    <span class="fake-square"></span>
                    <span class="window-control">×</span>
                </div>


                <div class="player-inside">

                    <section class="player">

                        <div class="track-info">

                            <div class="music-note">
                                ♫
                            </div>

                            <div>

                                <div
                                    class="song-title"
                                    id="songTitle"
                                >
                                    our song
                                </div>

                                <div
                                    class="artist"
                                    id="artist"
                                >
                                    Taylor Swift ♡
                                </div>

                            </div>

                        </div>


                        <div class="controls-section">

                            <div class="main-controls">

                                <button
                                    type="button"
                                    class="control-button"
                                    id="prevButton"
                                >
                                    |◀
                                </button>

                                <button
                                    type="button"
                                    class="control-button play-button"
                                    id="playButton"
                                >
                                    ▶
                                </button>

                                <button
                                    type="button"
                                    class="control-button"
                                    id="nextButton"
                                >
                                    ▶|
                                </button>

                            </div>


                            <div class="progress-row">

                                <span id="currentTime">
                                    0:00
                                </span>

                                <div
                                    class="progress-track"
                                    id="progressTrack"
                                >

                                    <div
                                        class="progress-fill"
                                        id="progressFill"
                                    >
                                        <div class="progress-dot"></div>
                                    </div>

                                </div>

                                <span id="totalTime">
                                    0:00
                                </span>

                            </div>

                        </div>


                        <div class="right-controls">

                            <span class="volume">
                                ◖))
                            </span>

                            <span class="player-heart">
                                ♡
                            </span>

                        </div>

                    </section>


                    <audio
                        id="audio"
                        preload="metadata"
                    ></audio>

                </div>

            </section>

        </section>

    </main>

</div>


<script>

/* ========================================================
   DATA
======================================================== */

const letters = __LETTERS_JSON__;
const order = ["1", "2", "3"];

let currentLetterId = "1";


/* ========================================================
   ELEMENTS
======================================================== */

const envelopes =
    document.querySelectorAll(".envelope-item");

const paper =
    document.getElementById("paper");

const paperScroll =
    document.getElementById("paperScroll");

const letterText =
    document.getElementById("letterText");

const letterPolaroids =
    document.getElementById("letterPolaroids");

const letterStamps =
    document.getElementById("letterStamps");

const signature =
    document.getElementById("signature");

const songTitle =
    document.getElementById("songTitle");

const artist =
    document.getElementById("artist");

const audio =
    document.getElementById("audio");

const playButton =
    document.getElementById("playButton");

const prevButton =
    document.getElementById("prevButton");

const nextButton =
    document.getElementById("nextButton");

const progressTrack =
    document.getElementById("progressTrack");

const progressFill =
    document.getElementById("progressFill");

const currentTimeLabel =
    document.getElementById("currentTime");

const totalTimeLabel =
    document.getElementById("totalTime");


/* ========================================================
   TIME FORMAT
======================================================== */

function formatTime(seconds) {

    if (!Number.isFinite(seconds)) {
        return "0:00";
    }

    const minutes =
        Math.floor(seconds / 60);

    const secs =
        Math.floor(seconds % 60)
        .toString()
        .padStart(2, "0");

    return `${minutes}:${secs}`;
}


/* ========================================================
   OPTIONAL POLAROID / STAMP RENDERERS
======================================================== */

function renderPolaroids(items) {

    letterPolaroids.replaceChildren();

    const validItems =
        Array.isArray(items)
        ? items.filter(
            item =>
                item &&
                item.image
        )
        : [];

    letterPolaroids.classList.toggle(
        "has-items",
        validItems.length > 0
    );

    validItems.forEach(
        (item, index) => {

            const card =
                document.createElement(
                    "figure"
                );

            card.className =
                "polaroid";


            const x =
                Number(item.x) || 0;

            const y =
                Number(item.y) || 0;

            const width =
                Math.max(
                    80,
                    Number(item.width) || 190
                );

            const height =
                Math.max(
                    60,
                    Number(item.height) || 170
                );

            const rotation =
                Number(item.rotation) || 0;


            card.style.setProperty(
                "--polaroid-x",
                `${x}px`
            );

            card.style.setProperty(
                "--polaroid-y",
                `${y}px`
            );

            card.style.setProperty(
                "--polaroid-width",
                `${width}px`
            );

            card.style.setProperty(
                "--polaroid-height",
                `${height}px`
            );

            card.style.setProperty(
                "--polaroid-rotation",
                `${rotation}deg`
            );


            const image =
                document.createElement(
                    "img"
                );

            image.src =
                item.image;

            image.alt =
                item.alt ||
                `Letter photo ${index + 1}`;

            image.loading =
                "lazy";


            const caption =
                document.createElement(
                    "figcaption"
                );

            caption.className =
                "polaroid-caption";

            caption.textContent =
                item.caption || "";


            card.appendChild(
                image
            );

            card.appendChild(
                caption
            );

            letterPolaroids.appendChild(
                card
            );
        }
    );
}


function renderStamps(items) {

    letterStamps.replaceChildren();

    const validItems =
        Array.isArray(items)
        ? items.filter(
            item =>
                item &&
                item.image
        )
        : [];

    letterStamps.classList.toggle(
        "has-items",
        validItems.length > 0
    );

    validItems.forEach(
        (item, index) => {

            const frame =
                document.createElement(
                    "div"
                );

            frame.className =
                "stamp";


            const x =
                Number(item.x) || 0;

            const y =
                Number(item.y) || 0;

            const width =
                Math.max(
                    30,
                    Number(item.width) || 74
                );

            const height =
                Math.max(
                    30,
                    Number(item.height) || 92
                );

            const rotation =
                Number(item.rotation) || 0;


            frame.style.setProperty(
                "--stamp-x",
                `${x}px`
            );

            frame.style.setProperty(
                "--stamp-y",
                `${y}px`
            );

            frame.style.setProperty(
                "--stamp-width",
                `${width}px`
            );

            frame.style.setProperty(
                "--stamp-height",
                `${height}px`
            );

            frame.style.setProperty(
                "--stamp-rotation",
                `${rotation}deg`
            );


            const image =
                document.createElement(
                    "img"
                );

            image.src =
                item.image;

            image.alt =
                item.alt ||
                `Letter stamp ${index + 1}`;

            image.loading =
                "lazy";


            frame.appendChild(
                image
            );

            letterStamps.appendChild(
                frame
            );
        }
    );
}


/* ========================================================
   LETTER DISPLAY
======================================================== */

function updateLetterDisplay(letter) {

    paper.classList.add(
        "paper-changing"
    );

    setTimeout(() => {

        /* Every newly opened letter begins at the top. */
        paperScroll.scrollTop = 0;

        letterText.textContent =
            letter.text;

        renderPolaroids(
            letter.polaroids
        );

        renderStamps(
            letter.stamps
        );

        signature.textContent =
            letter.signature;

        songTitle.textContent =
            letter.song_title;

        artist.textContent =
            letter.artist;

        paper.classList.remove(
            "paper-changing"
        );

        resizeStreamlitFrame();

    }, 220);
}


/* ========================================================
   LOAD MUSIC AT ASSIGNED START TIME
======================================================== */

async function loadSong(letter, shouldAutoplay) {

    audio.pause();

    playButton.textContent =
        "▶";

    progressFill.style.width =
        "0%";

    currentTimeLabel.textContent =
        "0:00";

    totalTimeLabel.textContent =
        "0:00";


    if (!letter.audio) {

        audio.removeAttribute("src");
        audio.load();

        return;
    }


    const startTime =
        Math.max(
            0,
            Number(letter.start_time) || 0
        );


    /*
    Mute while loading so the visitor does not hear the
    first fraction of the song before the seek finishes.
    */

    audio.volume = 0;

    audio.src =
        letter.audio;

    audio.load();


    /*
    IMPORTANT:
    audio.play() is called immediately from the click
    interaction. This gives browsers the best chance of
    allowing automatic playback.
    */

    let playPromise = null;

    if (shouldAutoplay) {

        try {

            playPromise =
                audio.play();

        } catch (error) {

            console.log(
                "Playback could not be requested."
            );
        }
    }


    const prepareStartPosition = () => {

        const safeStart =
            Number.isFinite(audio.duration) &&
            audio.duration > 0
                ? Math.min(
                    startTime,
                    Math.max(
                        0,
                        audio.duration - 0.05
                    )
                )
                : startTime;


        audio.currentTime =
            safeStart;


        currentTimeLabel.textContent =
            formatTime(safeStart);


        /*
        Wait until the seek has finished before unmuting.
        */

        const unmute = () => {
            audio.volume = 1;
        };


        if (Math.abs(audio.currentTime - safeStart) < 0.15) {
            audio.volume = 1;
        } else {
            audio.addEventListener(
                "seeked",
                unmute,
                { once: true }
            );
        }
    };


    if (audio.readyState >= 1) {

        prepareStartPosition();

    } else {

        audio.addEventListener(
            "loadedmetadata",
            prepareStartPosition,
            { once: true }
        );
    }


    if (
        shouldAutoplay &&
        playPromise &&
        typeof playPromise.then === "function"
    ) {

        try {

            await playPromise;

            playButton.textContent =
                "❚❚";

        } catch (error) {

            /*
            Some browsers may still block autoplay.
            The song will remain positioned at the assigned
            start time, and the visitor can press Play.
            */

            playButton.textContent =
                "▶";

            console.log(
                "Browser blocked automatic playback."
            );
        }
    }
}


/* ========================================================
   OPEN A LETTER
======================================================== */

async function loadLetter(id, shouldAutoplay) {

    currentLetterId =
        id;

    const letter =
        letters[id];

    updateLetterDisplay(
        letter
    );

    await loadSong(
        letter,
        shouldAutoplay
    );
}


/* ========================================================
   ENVELOPE CLICK
======================================================== */

envelopes.forEach(envelope => {

    envelope.addEventListener(
        "click",
        () => {

            loadLetter(
                envelope.dataset.letter,
                true
            );
        }
    );


    envelope.addEventListener(
        "keydown",
        event => {

            if (
                event.key === "Enter" ||
                event.key === " "
            ) {

                event.preventDefault();

                loadLetter(
                    envelope.dataset.letter,
                    true
                );
            }
        }
    );
});


/* ========================================================
   PLAY / PAUSE
======================================================== */

playButton.addEventListener(
    "click",
    async () => {

        if (!audio.getAttribute("src")) {
            return;
        }

        if (audio.paused) {

            try {

                await audio.play();

                playButton.textContent =
                    "❚❚";

            } catch (error) {

                console.log(
                    "Audio playback could not start."
                );
            }

        } else {

            audio.pause();

            playButton.textContent =
                "▶";
        }
    }
);


/* ========================================================
   METADATA / DURATION
======================================================== */

audio.addEventListener(
    "loadedmetadata",
    () => {

        totalTimeLabel.textContent =
            formatTime(
                audio.duration
            );
    }
);


/* ========================================================
   AUDIO PROGRESS
======================================================== */

audio.addEventListener(
    "timeupdate",
    () => {

        currentTimeLabel.textContent =
            formatTime(
                audio.currentTime
            );

        if (
            Number.isFinite(audio.duration) &&
            audio.duration > 0
        ) {

            const percent =
                (
                    audio.currentTime /
                    audio.duration
                ) * 100;

            progressFill.style.width =
                `${percent}%`;
        }
    }
);


/* ========================================================
   SONG ENDED
======================================================== */

audio.addEventListener(
    "ended",
    () => {

        playButton.textContent =
            "▶";
    }
);


/* ========================================================
   CLICK PROGRESS BAR
======================================================== */

progressTrack.addEventListener(
    "click",
    event => {

        if (
            !Number.isFinite(audio.duration) ||
            audio.duration <= 0
        ) {
            return;
        }

        const rect =
            progressTrack.getBoundingClientRect();

        const ratio =
            Math.min(
                1,
                Math.max(
                    0,
                    (
                        event.clientX -
                        rect.left
                    ) / rect.width
                )
            );

        audio.currentTime =
            ratio * audio.duration;
    }
);


/* ========================================================
   PREVIOUS / NEXT LETTER
======================================================== */

prevButton.addEventListener(
    "click",
    () => {

        let index =
            order.indexOf(
                currentLetterId
            );

        index =
            (
                index -
                1 +
                order.length
            ) % order.length;

        loadLetter(
            order[index],
            true
        );
    }
);


nextButton.addEventListener(
    "click",
    () => {

        let index =
            order.indexOf(
                currentLetterId
            );

        index =
            (
                index + 1
            ) % order.length;

        loadLetter(
            order[index],
            true
        );
    }
);


/* ========================================================
   STREAMLIT FRAME HEIGHT
   Keep one normal page scrollbar on desktop and phone.
======================================================== */

let frameResizeTimer = null;

function resizeStreamlitFrame() {

    clearTimeout(frameResizeTimer);

    frameResizeTimer = setTimeout(() => {

        const app =
            document.getElementById("letter-app");

        if (!app) {
            return;
        }

        const contentHeight =
            Math.ceil(
                Math.max(
                    app.scrollHeight,
                    app.offsetHeight,
                    document.body.scrollHeight,
                    document.documentElement.scrollHeight
                )
            );

        window.parent.postMessage(
            {
                isStreamlitMessage: true,
                type: "streamlit:setFrameHeight",
                height: contentHeight
            },
            "*"
        );

    }, 40);
}


window.addEventListener(
    "load",
    () => {
        resizeStreamlitFrame();

        setTimeout(resizeStreamlitFrame, 150);
        setTimeout(resizeStreamlitFrame, 500);
        setTimeout(resizeStreamlitFrame, 1200);
    }
);

window.addEventListener(
    "resize",
    resizeStreamlitFrame
);

if ("ResizeObserver" in window) {

    const appResizeObserver =
        new ResizeObserver(
            resizeStreamlitFrame
        );

    appResizeObserver.observe(
        document.getElementById("letter-app")
    );
}


/* ========================================================
   INITIAL PAGE
   Show letter 1, but DON'T autoplay before any click.
======================================================== */

loadLetter(
    "1",
    false
);

resizeStreamlitFrame();

</script>
"""


# =========================================================
# INSERT PYTHON DATA INTO HTML SAFELY
# =========================================================

html = html.replace(
    "__LETTERS_JSON__",
    letters_json,
)


# =========================================================
# RENDER
# =========================================================

components.html(
    html,
    # Large fallback height for phones. Because scrolling=False,
    # this does NOT create an iframe scrollbar; the normal Streamlit/browser
    # page scroll is used. The JS above will reduce/adjust the frame height
    # automatically where Streamlit permits it.
    height=2200,
    scrolling=False,
)
