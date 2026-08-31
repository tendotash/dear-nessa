import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dear Nessa",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide normal Streamlit UI
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .stApp {
            background:
                radial-gradient(circle at 20% 20%, #24192f 0%, transparent 35%),
                radial-gradient(circle at 80% 70%, #211326 0%, transparent 35%),
                #0d0b13;
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 1rem;
            max-width: 1500px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

html = """
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: transparent;
    color: #f7eaf7;
    font-family: Georgia, "Times New Roman", serif;
}

.website {
    width: 100%;
    max-width: 1250px;
    margin: 0 auto;
    padding: 20px;
}

/* ===============================
   MAIN LAYOUT
================================ */

.workspace {
    display: grid;
    grid-template-columns: 0.92fr 1.08fr;
    gap: 28px;
    align-items: start;
}

/* ===============================
   FAKE WINDOW
================================ */

.window {
    border: 1.5px solid #be8acb;
    border-radius: 14px;
    background: rgba(23, 15, 31, 0.72);
    box-shadow:
        0 0 25px rgba(187, 124, 205, 0.08),
        inset 0 0 35px rgba(255,255,255,0.015);
    overflow: hidden;
}

.window-bar {
    height: 38px;
    border-bottom: 1px solid #8d6398;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 12px;
    gap: 8px;
}

.window-control {
    color: #dfbce6;
    font-family: Arial, sans-serif;
    font-size: 17px;
    opacity: 0.9;
}

/* ===============================
   LEFT ENVELOPES
================================ */

.envelope-area {
    min-height: 850px;
    padding: 60px 35px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.envelope-wrap {
    position: relative;
    width: 310px;
    height: 205px;
    cursor: pointer;
    margin: 35px 0;
}

.envelope-wrap:focus-visible {
    outline: 3px solid #e4b4ef;
    outline-offset: 9px;
    border-radius: 10px;
}

/* letter hidden behind envelope */

.peek-letter {
    position: absolute;
    width: 190px;
    height: 135px;
    left: 60px;
    bottom: 35px;
    background: #f7e9d7;
    color: #352935;
    padding: 17px;
    border-radius: 5px;
    font-size: 15px;
    line-height: 1.45;
    transition:
        transform 0.55s cubic-bezier(.2,.8,.2,1),
        opacity 0.3s ease;
    z-index: 1;
    opacity: 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

.envelope-wrap:hover .peek-letter,
.envelope-wrap:focus .peek-letter {
    transform: translateY(-115px);
    opacity: 1;
}

/* envelope body */

.envelope {
    width: 310px;
    height: 190px;
    position: absolute;
    bottom: 0;
    border-radius: 8px;
    overflow: hidden;
    z-index: 3;
    box-shadow:
        0 15px 28px rgba(0,0,0,0.35),
        0 0 25px rgba(232,175,225,0.09);

    transition:
        transform 0.35s ease,
        filter 0.35s ease;
}

.envelope-wrap:hover .envelope {
    transform: translateY(8px) scale(1.025);
    filter: brightness(1.08);
}

/* colour variations */

.pink {
    background: linear-gradient(
        145deg,
        #efa9bc,
        #cf7698
    );
}

.cream {
    background: linear-gradient(
        145deg,
        #f3dfc4,
        #d8b895
    );
}

.lilac {
    background: linear-gradient(
        145deg,
        #d8b7ea,
        #a77bc1
    );
}

/* envelope diagonal folds */

.envelope::before {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    left: -100px;
    top: 25px;
    transform: rotate(45deg);
    border-top: 2px solid rgba(74, 44, 75, 0.38);
    border-right: 2px solid rgba(74, 44, 75, 0.30);
}

.envelope::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    right: -100px;
    top: 25px;
    transform: rotate(-45deg);
    border-top: 2px solid rgba(74, 44, 75, 0.38);
    border-left: 2px solid rgba(74, 44, 75, 0.30);
}

/* top triangular flap */

.flap {
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;

    border-left: 155px solid transparent;
    border-right: 155px solid transparent;
    border-top: 112px solid rgba(255,255,255,0.18);

    filter: drop-shadow(0px 2px 1px rgba(80,45,72,0.45));
    z-index: 5;
}

/* little icons */

.envelope-icon {
    position: absolute;
    bottom: 18px;
    right: 20px;
    color: #3b2640;
    z-index: 9;
    font-family: Arial, sans-serif;
    font-size: 32px;
}

.smiley {
    font-size: 29px;
}

.stars {
    font-size: 24px;
    letter-spacing: -5px;
}

/* ===============================
   RIGHT SIDE
================================ */

.right-side {
    display: flex;
    flex-direction: column;
    gap: 25px;
}

/* ===============================
   PREVIEW WINDOW
================================ */

.preview-content {
    min-height: 275px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 35px;
}

.mini-letter {
    width: 220px;
    min-height: 175px;
    background: #f3dfca;
    color: #3a2c3b;
    padding: 25px 24px;
    box-shadow:
        0 12px 30px rgba(0,0,0,0.25),
        0 0 22px rgba(244,209,224,0.08);
    line-height: 1.55;
    transform: rotate(-1deg);
}

.preview-label {
    margin-left: 35px;
    color: #deb2db;
    font-size: 18px;
    line-height: 1.6;
}

/* ===============================
   FULL LETTER
================================ */

.letter-window-content {
    padding: 40px;
}

.paper {
    position: relative;
    max-width: 520px;
    margin: 0 auto;

    background:
        linear-gradient(
            rgba(248, 231, 210, 0.96),
            rgba(239, 216, 191, 0.96)
        );

    color: #312536;

    padding: 55px 50px 65px;
    min-height: 510px;

    clip-path: polygon(
        1% 1%,
        8% 0%,
        15% 1%,
        23% 0%,
        31% 1%,
        40% 0%,
        49% 1%,
        58% 0%,
        67% 1%,
        77% 0%,
        86% 1%,
        94% 0%,
        99% 2%,
        100% 10%,
        99% 20%,
        100% 31%,
        99% 41%,
        100% 53%,
        99% 64%,
        100% 75%,
        99% 86%,
        100% 97%,
        94% 100%,
        84% 99%,
        75% 100%,
        64% 99%,
        54% 100%,
        43% 99%,
        32% 100%,
        22% 99%,
        11% 100%,
        1% 98%,
        0% 88%,
        1% 77%,
        0% 67%,
        1% 55%,
        0% 44%,
        1% 34%,
        0% 22%,
        1% 12%
    );

    box-shadow: 0 18px 35px rgba(0,0,0,0.35);

    transition:
        opacity .35s ease,
        transform .35s ease;
}

.paper.change {
    opacity: 0;
    transform: translateY(10px);
}

.letter-text {
    font-size: 21px;
    line-height: 1.9;
    white-space: pre-line;
}

.letter-signature {
    text-align: right;
    margin-top: 35px;
    font-size: 21px;
}

/* ===============================
   MUSIC
================================ */

.music-player {
    max-width: 520px;
    margin: 25px auto 5px;
    padding: 17px 20px;

    border: 1px solid #8f699a;
    border-radius: 16px;

    display: flex;
    align-items: center;
    gap: 16px;

    color: #e7cce8;
    background: rgba(33, 22, 42, 0.85);
}

.play-button {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    border: 1px solid #cda4d6;
    background: transparent;
    color: #f3ddf4;
    font-size: 18px;
    cursor: pointer;
}

.play-button:hover {
    background: rgba(221,179,232,.12);
}

.song-area {
    flex: 1;
}

.song-name {
    font-size: 16px;
    margin-bottom: 8px;
}

.song-line {
    width: 100%;
    height: 3px;
    background: #75597a;
    border-radius: 50px;
}

.song-progress {
    width: 34%;
    height: 100%;
    background: #d9afd9;
    border-radius: 50px;
}

/* ===============================
   INTRO / INSTRUCTION
================================ */

.small-note {
    text-align: center;
    color: #bda7c0;
    font-size: 15px;
    margin: 3px 0 20px;
}

/* ===============================
   MOBILE
================================ */

@media (max-width: 850px) {

    .website {
        padding: 8px;
    }

    .workspace {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .envelope-area {
        min-height: auto;
        padding: 40px 15px;
    }

    .envelope-wrap {
        transform: scale(.86);
        margin: 25px 0;
    }

    .preview-content {
        min-height: 220px;
        padding: 20px;
    }

    .preview-label {
        font-size: 15px;
        margin-left: 18px;
    }

    .letter-window-content {
        padding: 20px;
    }

    .paper {
        padding: 42px 32px 50px;
        min-height: 430px;
    }

    .letter-text,
    .letter-signature {
        font-size: 18px;
    }
}

</style>


<div class="website">

    <div class="small-note">
        hover over an envelope ♡
    </div>

    <div class="workspace">

        <!-- =====================
             LEFT WINDOW
        ====================== -->

        <section class="window">

            <div class="window-bar">
                <span class="window-control">—</span>
                <span class="window-control">□</span>
                <span class="window-control">×</span>
            </div>

            <div class="envelope-area">

                <!-- Envelope 1 -->

                <div
                    class="envelope-wrap"
                    tabindex="0"
                    data-letter="1"
                >

                    <div class="peek-letter">
                        Dear N,<br><br>
                        You did great today & it is all going to...
                    </div>

                    <div class="envelope pink">
                        <div class="flap"></div>
                        <div class="envelope-icon">♡</div>
                    </div>

                </div>


                <!-- Envelope 2 -->

                <div
                    class="envelope-wrap"
                    tabindex="0"
                    data-letter="2"
                >

                    <div class="peek-letter">
                        Dear N,<br><br>
                        I hope you know how much you mean...
                    </div>

                    <div class="envelope cream">
                        <div class="flap"></div>
                        <div class="envelope-icon smiley">☺</div>
                    </div>

                </div>


                <!-- Envelope 3 -->

                <div
                    class="envelope-wrap"
                    tabindex="0"
                    data-letter="3"
                >

                    <div class="peek-letter">
                        Dear N,<br><br>
                        Just a little letter for you...
                    </div>

                    <div class="envelope lilac">
                        <div class="flap"></div>
                        <div class="envelope-icon stars">☆ ☆</div>
                    </div>

                </div>

            </div>

        </section>


        <!-- =====================
             RIGHT SIDE
        ====================== -->

        <div class="right-side">

            <!-- PREVIEW -->

            <section class="window">

                <div class="window-bar">
                    <span class="window-control">—</span>
                    <span class="window-control">□</span>
                    <span class="window-control">×</span>
                </div>

                <div class="preview-content">

                    <div
                        class="mini-letter"
                        id="previewLetter"
                    >
                        Dear N,<br><br>
                        You did great today & it is all going to...
                    </div>

                    <div class="preview-label">
                        preview<br>
                        click the envelope<br>
                        to open it fully ♡
                    </div>

                </div>

            </section>


            <!-- FULL LETTER -->

            <section class="window">

                <div class="window-bar">
                    <span class="window-control">—</span>
                    <span class="window-control">□</span>
                    <span class="window-control">×</span>
                </div>

                <div class="letter-window-content">

                    <div
                        class="paper"
                        id="paper"
                    >

                        <div
                            class="letter-text"
                            id="letterText"
                        >Dear N,

You did great today & it is
all going to be okay!

Believe in yourself & keep
going. Good things take time.</div>

                        <div
                            class="letter-signature"
                            id="letterSignature"
                        >
                            Love, R ♡
                        </div>

                    </div>


                    <div class="music-player">

                        <button
                            class="play-button"
                            id="playButton"
                            type="button"
                        >
                            ▶
                        </button>

                        <div class="song-area">

                            <div
                                class="song-name"
                                id="songName"
                            >
                                ♫ your song
                            </div>

                            <div class="song-line">
                                <div class="song-progress"></div>
                            </div>

                        </div>

                        <div>♡</div>

                    </div>

                </div>

            </section>

        </div>

    </div>

</div>


<script>

const letters = {

    1: {
        preview:
            "Dear N,<br><br>You did great today & it is all going to...",

        text:
`Dear N,

You did great today & it is
all going to be okay!

Believe in yourself & keep
going. Good things take time.`,

        signature:
            "Love, R ♡",

        song:
            "♫ your song"
    },


    2: {
        preview:
            "Dear N,<br><br>I hope you know how much you mean...",

        text:
`Dear N,

I hope you know how important
you are.

Some days might feel ordinary,
but having you around makes
them much less ordinary.

Never forget how loved and
appreciated you are.`,

        signature:
            "Love, R ☺",

        song:
            "♫ another song"
    },


    3: {
        preview:
            "Dear N,<br><br>Just a little letter for you...",

        text:
`Dear N,

This is just a little reminder
that I am always cheering
for you.

Take your time.
Keep going.
And remember to be kind
to yourself too.`,

        signature:
            "Love, R ☆",

        song:
            "♫ our song"
    }

};


const preview =
    document.getElementById("previewLetter");

const paper =
    document.getElementById("paper");

const letterText =
    document.getElementById("letterText");

const signature =
    document.getElementById("letterSignature");

const songName =
    document.getElementById("songName");

const envelopes =
    document.querySelectorAll(".envelope-wrap");


envelopes.forEach(envelope => {

    /* Hover preview */

    envelope.addEventListener(
        "mouseenter",
        function() {

            const id =
                this.dataset.letter;

            preview.innerHTML =
                letters[id].preview;
        }
    );


    /* Click opens full letter */

    envelope.addEventListener(
        "click",
        function() {

            const id =
                this.dataset.letter;

            paper.classList.add("change");

            setTimeout(() => {

                letterText.textContent =
                    letters[id].text;

                signature.textContent =
                    letters[id].signature;

                songName.textContent =
                    letters[id].song;

                paper.classList.remove("change");

            }, 200);

        }
    );


    /* Keyboard accessibility */

    envelope.addEventListener(
        "keydown",
        function(event) {

            if (
                event.key === "Enter" ||
                event.key === " "
            ) {

                event.preventDefault();
                this.click();

            }

        }
    );

});


const playButton =
    document.getElementById("playButton");

let playing = false;

playButton.addEventListener(
    "click",
    function() {

        playing = !playing;

        playButton.textContent =
            playing ? "❚❚" : "▶";

    }
);

</script>
"""

components.html(
    html,
    height=1200,
    scrolling=True
)
