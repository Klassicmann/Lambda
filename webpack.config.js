module.exports ={
    entry: "./Lambda-master/frontend/src/index.js",
    module:{
        rules: [
            {
                test: /\.js$/,
                exclude:/node_modules/,
                use:{
                    loader: "babel-loader"
                }
            }
        ]
    }
}