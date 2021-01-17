// alert("Grr.");
whiteList = ["google.ca"];

chrome.tabs.onActivated.addListener(function (activeInfo) {
  chrome.tabs.get(activeInfo.tabId, function (tab) {
    y = tab.url;
    urlObject = new URL(y);
    hostnameString = urlObject.hostname.toString();

    whiteList.push(hostnameString);

    // alert(whiteList);
    // saveWhitelist(whiteList);
    // searchWhitelist(hostnameString);

    // var testArray = ["test", "teste", "testes"];

    chrome.storage.sync.set(
      {
        list: whiteList,
      },
      function () {
        // alert(whiteList);
      }
    );

    chrome.storage.sync.get(
      {
        whiteList: [], //put defaultvalues if any
      },

      function (data) {
        console.log(data.list);
        update(data.list); //storing the storage value in a variable and passing to update function
      }
    );

    function update(array) {
      array.push("testAdd");
      //then call the set to update with modified value
      chrome.storage.sync.set(
        {
          list: array,
        },
        function () {
          console.log("added to list with new values");
        }
      );
    }
  });
});
