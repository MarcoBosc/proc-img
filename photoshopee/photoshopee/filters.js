function convertToGrayscale(matrix) {
    console.log("chegou aqui")
    console.log(matrix)

    let grayscaleMatrix = [];
    for (let i = 0; i < matrix.length; i++) { // Itera sobre as linhas da matriz
        let row = matrix[i];
        let grayscaleRow = [];
        for (let j = 0; j < row.length; j++) { // Itera sobre os pixels na linha atual
            let pixel = row[j];
            let r = pixel[0]; 
            let g = pixel[1];
            let b = pixel[2];

            if (0 <= r && r <= 255 && 0 <= g && g <= 255 && 0 <= b && b <= 255) {
                let grayScale = Math.round((r + g + b) / 3); // Arredonda para o inteiro mais próximo
                grayscaleRow.push(grayScale);
            } else {
                console.log("Os valores devem estar entre 0 e 255.");
                return null;
            }
        }
        grayscaleMatrix.push(grayscaleRow);
    }
    console.log(grayscaleMatrix)
    return grayscaleMatrix;
}

export { convertToGrayscale };
