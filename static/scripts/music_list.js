let music_list = document.getElementsByClassName('music_list')[0]

const response = fetch('http://127.0.0.1:8000/rest/music/',{method: "GET"}).then(res => res.json())
  .then(function(data){
    data.forEach(element => {
        let music_card = document.createElement('div')
        music_card.className = 'music_card';
            let left = document.createElement('div')
            left.className = 'left'
                let left_img = document.createElement('img')
                left_img.src = element.cover
                left.appendChild(left_img)
            music_card.appendChild(left)

            let right = document.createElement('div')
            right.className = 'right'
                let rigth_top = document.createElement('div')
                rigth_top.className = 'right_top'
                    let title = document.createElement('div')
                    title.className = 'title'
                        let p_title = document.createElement('p')
                        p_title.innerHTML = element.title
                        title.appendChild(p_title)
                    rigth_top.appendChild(title)

                    let author = document.createElement('div')
                    author.className = 'author'
                        let p_author = document.createElement('p')
                        p_author.innerHTML = 'by '+element.author
                        author.appendChild(p_author)
                    rigth_top.appendChild(author)
                right.appendChild(rigth_top)

                let right_bottom = document.createElement('div')
                right_bottom.className = 'right_bottom'
                    let play = document.createElement('div')
                    play.className = 'play'
                        let button_play = document.createElement('input')
                        button_play.className = 'button_play'
                        button_play.type = 'button'
                        button_play.value = 'Play'
                        play.appendChild(button_play)
                    right_bottom.appendChild(play)

                    let duration = document.createElement('div')
                    duration.className = 'duration'
                        let range = document.createElement('audio')
                        range.className = 'audio'
                        range.src = element.file
                        console.log(element.file)
                        duration.appendChild(range)
                    right_bottom.appendChild(duration)
                right.appendChild(right_bottom)
            music_card.appendChild(right)

        music_list.appendChild(music_card)

    });
    return data
  })
