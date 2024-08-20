function handleFileSelect(ele){
    var file = ele.target.files[0];
    print("Rishu Filename"+file)
    var fileReader = new FileReader();
    fileReader.readAsDataURL(file)
    fileReader.onload = () => {
        var arrayBuffer = fileReader.result; 
        socketControl.uploadImage({ 
            name: file.name, 
            type: file.type, 
            size: file.size, 
            binary: arrayBuffer 
         });
     }
}
