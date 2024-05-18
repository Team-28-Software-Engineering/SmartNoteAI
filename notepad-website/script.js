function toggleDownloadInfo(os) {
    const infoElement = document.getElementById(`${os}-download-info`);
    const arrowElement = document.getElementById(`${os}-info`);

    if (infoElement.classList.contains('hidden')) {
        infoElement.classList.remove('hidden');
        arrowElement.innerHTML = '&#9650;'; 
    } else {
        infoElement.classList.add('hidden');
        arrowElement.innerHTML = '&#9660;'; 
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const content = document.getElementById("content");

    const sections = {
        home: `
            <div class="fade-in">
                <div class="heading">Notepad with AI</div>
                <p>The "Notepad with AI" project: revolutionizing note-taking in the digital era. This innovative tool combines traditional note-taking with advanced AI capabilities to enhance productivity and efficiency.
                 With intelligent note categorization, natural language processing for easy input, and smart search functionality, finding and organizing notes has never been easier. The notepad learns from user behavior to offer personalized insights and recommendations, ensuring a seamless and tailored experience. 
                 Compatible across devices, it syncs effortlessly, keeping notes accessible anytime, anywhere. Say hello to a more organized, efficient, and personalized note-taking experience with the "Notepad with AI."</p>
                <div class="image-gallery">
                    <img src="anhHome.png" alt="Screenshot 1" class="gallery-item"><br>
                </div>
            </div>
        `,
        download: `
            <div class="fade-in">
                <div class="heading">Downloads</div>
                <p><a href="notepadsetup.exe" onclick="toggleDownloadInfo('windows')">Download Notepad v0.0.1 for Windows <span id="windows-info" class="arrow">&#9660;</span></a></p>
                <div id="windows-download-info" class="hidden">
                    <p>Hướng dẫn cài ứng dụng trên Windows</p>
                    <p>File .exe sẽ được tải về máy</p>
                    <p>Hình bên dưới minh họa các bước cài đặt phần mềm trên Window</p>
                </div>
                
                <p><a href="notepadsetup.exe" onclick="toggleDownloadInfo('linux')">Download Notepad v0.0.1 for Linux <span id="linux-info" class="arrow">&#9660;</span></a></p>
                <div id="linux-download-info" class="hidden">
                    <p>Hướng dẫn cài ứng dụng trên Linux</p>
                    <p>Mở terminal và chạy những dòng lệnh sau</p>
                    <p>1. sudo apt update</p>
                    <p>2. sudo apt-get install wine</p>
                    <p>3. sudo apt-get install wine32</p>
                    <p>4. sudo apt-get install libwine</p>
                    <p>Hãy tìm đến thư mục chứa tập exe vừa tải và chạy dòng lệnh sau</p>
                    <p>5. wine notepadsetup.exe</p>
                </div>

                <p><a href="notepadsetup.exe" onclick="toggleDownloadInfo('macos')">Download Notepad v0.0.1 for MacOS <span id="macos-info" class="arrow">&#9660;</span></a></p>
                <div id="macos-download-info" class="hidden">
                    <p>Thông tin tải xuống cho MacOS</p>
                </div>
                
            </div>

            <p> </p>
            <p> Images of download on Windows </p>
            
            <div class="image-gallery">
                <img src="setup1.png" alt="Image 1" class="gallery-item"><br>
                <img src="setup2.png" alt="Image 2" class="gallery-item"><br>
                <img src="setup3.png" alt="Image 3" class="gallery-item"><br>
                <img src="setup4.png" alt="Image 4" class="gallery-item"><br>
                <img src="setup5.png" alt="Image 5" class="gallery-item"><br>
            </div>
        `,
        features: `
            <div class="fade-in">
                <div class="heading">Features of my software</div>
                <div class="features-section">
                    ${createFeatureHTML(1, 'Basic operations like creating notes, saving notes', 'feature1.png')}
                    ${createFeatureHTML(2, 'Search, cut, copy, paste, redo functions', 'feature2.png')}
                    ${createFeatureHTML(3, 'Text formatting: bold, italic, underline, change font color, choose font', 'feature3.png')}
                    ${createFeatureHTML(4, 'Count characters, words, lines', 'feature5.png')}
                    ${createFeatureHTML(5, 'Insert image', 'feature6.png')}
                    ${createFeatureHTML(6, 'Translation feature', 'feature7.png')}
                    ${createFeatureHTML(7, 'English spell check', 'feature8.png')}
                    ${createFeatureHTML(8, 'Chat with AI through ChatGPT API', 'feature9.png')}
                    ${createFeatureHTML(9, 'Image-to-text functionality', 'feature10.png')}
                    ${createFeatureHTML(10, 'Mp3-to-text functionality', 'feature11.png')}
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
