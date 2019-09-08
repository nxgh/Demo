class Carousel {
    constructor (obj) {
        this.wrap = obj.wrap;
        this.wrapId = obj.wrap.id;              //容器的id
        this.wrapWidth = this.wrap.offsetWidth; //容器宽
        this.wrapHeight = this.wrap.offsetHeight; //容器高
        this.imgCount = obj.imgArr.length;     //图片数
        this.activePage = 0;                    //轮播图当前页
        this.settimeID;                         //定时器id
        this.index = 1
        this.animated = false
        this.offset = -this.wrap.offsetWidth
        this.init(obj.imgArr)
    }
    init(imgArr) {
        this.wrap.style.position = "relative";
        this.wrap.style.overflow = "hidden";
        this.wrap.innerHTML = `
            <div id="${this.wrapId}_img_list" style="left:${this.offset}px; width:${this.wrapWidth * (this.imgCount + 2)}px; height: ${this.wrapHeight}px">
   
            </div>
            <div id="${this.wrapId}_dot" style="left: ${(this.wrapWidth-(this.imgCount*20))/2}px; width: ${this.imgCount*20}px; ">
                <span tyep="button" index="1" class="active" style="margin-left:5px;"></span>
            </div>
            <a id="${this.wrapId}_prev" class="arrow" style="top: ${(this.wrapHeight-80) / 2}px"><</a>
            <a id="${this.wrapId}_next" class="arrow" style="top: ${(this.wrapHeight-80) / 2}px">></a>
        `

        document.getElementById(`${this.wrapId}_img_list`).innerHTML += `
            <img src="${imgArr[imgArr.length - 1]}">
        `
        imgArr.forEach(element => {
            document.getElementById(`${this.wrapId}_img_list`).innerHTML += `
                <img src="${element}">
            `
        });
        document.getElementById(`${this.wrapId}_img_list`).innerHTML += `
            <img src="${imgArr[0]}">
        `
        for (let i = 1; i < this.imgCount; i++) {
            document.getElementById(`${this.wrapId}_dot`).innerHTML += `
                <span type="button" index=${i+1}></span>
            `
        }
        this.bindEvent()
    }
    bindEvent() {
        let prev = document.getElementById(`${this.wrapId}_prev`)
        let next = document.getElementById(`${this.wrapId}_next`)
        prev.addEventListener('click', () => {
            if (!this.animated) {
                if (this.index == 1)
                    this.index = this.imgCount
                else
                    this.index -= 1
            }
            // console.log('prev index', this.index)
            this.dotActive();
            this.animate(this.wrapWidth)
        })
        next.addEventListener('click', () => {
            if (!this.animated) {
                if (this.index == this.imgCount)
                this.index = 1
                else
                this.index += 1
            }
            console.log('next index', this.index)
            this.dotActive();
            this.animate(-this.wrapWidth)
        })

    }
    dotActive() {
        let dotspans = document.getElementById(`${this.wrapId}_dot`).getElementsByTagName('span')
        for (let i = 0; i < dotspans.length; i++) {
            dotspans[i].className = ""            
        }
        dotspans[this.index - 1].className = "active"
    }
    animate(offset){
        // offset 偏移量
        // 
        let list = document.getElementById(`${this.wrapId}_img_list`)
        // 新的图片位置
        let newLeft = parseInt(list.style.left) + offset;

        list.style.left=newLeft+"px"   
        console.log('newLeft out of if ',newLeft)
        if (newLeft == -this.wrapWidth*(this.imgCount+2)) {
            // console.log('newLeft in if ',newLeft)
            // console.log('最后一张跳转第一一张')
            list.style.left = -this.wrapWidth*2 +"px"
        };
        // 偏移量大于最后一张 imgCount * wrapWidth
        if (newLeft > -this.wrapWidth) {
            // console.log('newLeft in if ',newLeft)
            // console.log('第一一张跳转最后一张')
            list.style.left = -this.imgCount * this.wrapWidth+"px"
        };
    }
}