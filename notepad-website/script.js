document.addEventListener("DOMContentLoaded", () => {
    const content = document.getElementById("content");

    const sections = {
        home: `
            <div class="fade-in">
                <div class="heading">Notepad with AI</div>
                <p>The "Notepad with AI" project: revolutionizing note-taking in the digital era. This innovative tool combines traditional note-taking with advanced AI capabilities to enhance productivity and efficiency. With intelligent note categorization, natural language processing for easy input, and smart search functionality, finding and organizing notes has never been easier. The notepad learns from user behavior to offer personalized insights and recommendations, ensuring a seamless and tailored experience. Compatible across devices, it syncs effortlessly, keeping notes accessible anytime, anywhere. Say hello to a more organized, efficient, and personalized note-taking experience with the "Notepad with AI."</p>
                <div class="image-gallery">
                    <img src="screenshot1.png" alt="Screenshot 1" class="gallery-item"><br>
                    <img src="screenshot2.png" alt="Screenshot 2" class="gallery-item">
                </div>
            </div>
        `,
        download: `
            <div class="fade-in">
                <div class="heading">Downloads</div>
                <p><a href="notepad-windows.exe" onclick="return confirmDownload('Windows')">Download Notepad v0.0.1 for Windows</a></p>
                <p><a href="notepad-windows.exe" onclick="return confirmDownload('Linux')">Download Notepad v0.0.1 for Linux</a></p>
                <p><a href="notepad-windows.exe" onclick="return confirmDownload('MacOS')">Download Notepad v0.0.1 for MacOS</a></p>
            </div>
        `,
        features: `
            <div class="fade-in">
                <div class="heading">Features of my software</div>
                <div class="features-section">
                    ${createFeatureHTML(1, 'Basic operations like creating notes, saving notes', 'feature1.png')}
                    ${createFeatureHTML(2, 'Search, cut, copy, paste, redo functions', 'feature2.png')}
                    ${createFeatureHTML(3, 'Text formatting: bold, italic, underline, change font color, choose font', 'feature3.png')}
                    ${createFeatureHTML(4, 'Change background color', 'feature4.png')}
                    ${createFeatureHTML(5, 'Count characters, words, lines', 'feature5.png')}
                    ${createFeatureHTML(6, 'Insert image', 'feature6.png')}
                    ${createFeatureHTML(7, 'Translation feature', 'feature7.png')}
                    ${createFeatureHTML(8, 'English spell check', 'feature8.png')}
                    ${createFeatureHTML(9, 'Chat with AI through ChatGPT API', 'feature9.png')}
                    ${createFeatureHTML(10, 'Image-to-text functionality', 'feature10.png')}
                    ${createFeatureHTML(11, 'Voice-to-text functionality', 'feature11.png')}
                </div>
            </div>
        `,
        help: `
            <div class="fade-in">
                <div class="heading">Online Help</div>
                <form>
                    <input type="text" placeholder="Name" required>
                    <input type="email" placeholder="Email" required>
                    <input type="tel" placeholder="Phone">
                    <textarea placeholder="Questions" required></textarea>
                    <input type="submit" value="Submit">
                </form>
            </div>
        `,
        author: `
            <div class="fade-in">
                <div class="heading">Author</div>
                <p><strong>Team28 Software Engineer</strong></p>
                <p><strong>Address:</strong> UET-HN-VN</p>
                <p><strong>Contact me:</strong></p>
                <p>Email: <a href="mailto:Team28@gmail.com">Team28@gmail.com</a></p>
                <p>Github: <a href="https://github.com/note" target="_blank">https://github.com/note</a></p>
            </div>
        `
    };

    document.getElementById("home-btn").addEventListener("click", () => loadContent('home'));
    document.getElementById("download-btn").addEventListener("click", () => loadContent('download'));
    document.getElementById("features-btn").addEventListener("click", () => loadContent('features'));
    document.getElementById("help-btn").addEventListener("click", () => loadContent('help'));
    document.getElementById("author-btn").addEventListener("click", () => loadContent('author'));

    loadContent('home');

    function loadContent(section) {
        content.innerHTML = sections[section];
    }

    function confirmDownload(os) {
        return confirm(`Do you want to download Notepad for ${os}?`);
    }

    function createFeatureHTML(number, description, image) {
        return `
            <div class="feature slide-in">
                <div class="feature-text">${number}. ${description}</div>
                <div class="feature-media"><img src="${image}" alt="Feature ${number}"></div>
            </div>
        `;
    }
});
