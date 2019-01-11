const{ src, dest, series } = require('gulp')
const htmlmin = require('gulp-htmlmin');
const criticalgen = require('critical')

function critical(){
    return criticalgen.generate({
            inline: false,
            base: 'dist/',
            src: 'index.html',
            css: 'output/css/style.css',
            target: {css: 'dist/css/main.css', uncritical: 'dist/css/style.css'},
            minify: true,
            rebase: asset => asset.relativePath
        });
}

function copy() {
    return src(['./output/**', '!./output/**/**.html'])
        .pipe(dest('dist'));
}

function html() {
    return src('./output/**/*.html')
        .pipe(htmlmin({
            collapseWhitespace: true
        }))
        .pipe(dest('dist'));
}

exports.copy = copy;
exports.html = html;
exports.critical = critical;
exports.default =series(copy, html, critical);
