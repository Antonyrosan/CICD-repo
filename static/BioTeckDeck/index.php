<?php
$file = "data.csv";

// Create CSV if not present
if (!file_exists($file)) {
    file_put_contents($file, "title,description\n");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Welcome to BioTeckDeck - The future of biotechnology solutions.">
    <meta name="keywords" content="Biotech, Technology, Science, Innovation">
    <meta property="og:title" content="BioTeckDeck">
    <meta property="og:description" content="Explore cutting-edge biotech solutions with BioTeckDeck.">
    <meta property="og:image" content="/images/preview.jpg">
    <title>Search CSV - BioTeckDeck</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        #popup, #popup-overlay { display: none; }
        #popup {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000; text-align: center;
        }
        #popup-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5);
            z-index: 999;
        }
    </style>
</head>
<body class="container mt-4">
    <h2 class="text-center">Search & Filter CSV Data</h2>
    <div class="mb-3">
        <input type="text" id="search" class="form-control" placeholder="Search by title..." autocomplete="off">
    </div>
    <div class="mb-3">
        <label for="sort" class="form-label">Sort by:</label>
        <select id="sort" class="form-select">
            <option value="asc">A-Z</option>
            <option value="desc">Z-A</option>
        </select>
    </div>
    <div class="mb-3">
        <label for="letter" class="form-label">Filter by Alphabet:</label>
        <select id="letter" class="form-select">
            <option value="">All</option>
            <?php foreach (range('A', 'Z') as $letter): ?>
                <option value="<?php echo $letter; ?>"><?php echo $letter; ?></option>
            <?php endforeach; ?>
        </select>
    </div>
    <div id="results" class="row"></div>
    <div id="popup-overlay"></div>
    <div id="popup">
        <h5 id="popup-title"></h5>
        <p id="popup-description"></p>
        <button id="speak" class="btn btn-primary">🔊 Read Aloud</button>
        <button id="popup-close">Close</button>
    </div>
    <script>
        function fetchResults() {
            $.post("search.php", {
                query: $("#search").val(),
                sort: $("#sort").val(),
                letter: $("#letter").val()
            }, function(data) {
                $("#results").html(data);
            });
        }
        $(document).ready(function() {
            $("#search, #sort, #letter").on("input change", fetchResults);
            $(document).on("click", ".popup-trigger", function() {
                $("#popup-title").text($(this).data("title"));
                $("#popup-description").text($(this).data("description"));
                $("#popup-overlay, #popup").fadeIn();
            });
            $("#popup-close, #popup-overlay").on("click", function() {
                $("#popup-overlay, #popup").fadeOut();
            });
            $("#speak").on("click", function() {
                let speech = new SpeechSynthesisUtterance($("#popup-description").text());
                speech.lang = "en-US";
                speech.rate = 1;
                window.speechSynthesis.speak(speech);
            });
            fetchResults();
        });
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>