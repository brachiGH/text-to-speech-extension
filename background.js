chrome.contextMenus.create({
  id: "ReadSelectedText",
  title: "Read Out Loud",
  contexts: ["selection"]
});

const url = 'http://192.168.81.76:6789';

chrome.contextMenus.onClicked.addListener(function(info) {
  if (info.menuItemId === "ReadSelectedText") {
    console.log(info.selectionText);

    const data = {
      content: info.selectionText
    };

    const options = {
      method: 'POST',
      body: JSON.stringify(data)
    };

    fetch(url, options)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Response:', data);
      })
      .catch(error => {});
  }
});

