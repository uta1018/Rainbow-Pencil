# グローバル変数
frame_count = 0
save_count=1
red=0
green=0
blue=0
color_mode = 'rainbow'
mode = 'draw'
images = []

def setup() :
    size(800, 800)
    background(0)
    noSmooth()
    print(u"このアプリでは、マウスやキーボードを使ってイラスト・アニメーションの作成ができます。まずは、マウスを使って線を引いてみましょう！\nキーボードの上段の[Q～Eキー]でスタンプ、キーボードの中段の[A～Fキー]で太さの異なるペン、[G～Jキー]で太さの異なる消しゴムを選択できます。\nさらに、キーボードの中段の[K,Lキー]でペンの切り替え、キーボード下段の[Zキー]で画面のリセット、[Xキー]でイラストの保存、[N,Mキー]でカラーモードの切り替えができます。\nアニメーションに関する機能は、[Cキー]で保存したイラストのアニメーション作成、[V,Bキー]でアニメーションモードと描画モードの切り替えができます。\n自由な発想でお絵描きを楽しみましょう！\n")


def draw() :    
    global frame_count, text_display, text_timer,save_count, mode
    frameRate(60)
    textMode(CENTER)
    ellipseMode(CENTER)

    # イラストの描画
    if mode == 'draw':
        draw_illust()
    # アニメーションの再生
    elif mode == 'animation':
        draw_animation()
        
    # フレームカウントを増やす
    frame_count += 1



              
# イラスト描写          
def draw_illust():
  global frame_count,red,green,blue
  for i in range(800):
      color=255*i/800
      strokeWeight(3)
      
      if(color_mode == 'random'):
          colorMode(RGB)
          stroke(color+red,color+green,color+blue)
          fill(color+red,color+green,color+blue)
      elif(color_mode == 'rainbow'):
          colorMode(HSB)
          stroke(color,200,200)
          fill(color,200,200)
          
      if(mousePressed and mouseX==i):
          line(mouseX,mouseY,pmouseX,pmouseY)
      elif(keyPressed and key=='a'and mouseX==i):
          ellipse(mouseX,mouseY,10,10)
      elif(keyPressed and key=='s'and mouseX==i):
          ellipse(mouseX,mouseY,30,30)
      elif(keyPressed and key=='d'and mouseX==i):
          ellipse(mouseX,mouseY,50,50)
      elif(keyPressed and key=='f'and mouseX==i):
          ellipse(mouseX,mouseY,80,80)
      elif(keyPressed and key=='g'and mouseX==i):
          stroke(0)
          line(mouseX,mouseY,pmouseX,pmouseY)
      elif(keyPressed and key=='h'and mouseX==i):
          fill(0)
          stroke(0)
          ellipse(mouseX,mouseY,30,30)
      elif(keyPressed and key=='j'and mouseX==i):
          fill(0)
          stroke(0)
          ellipse(mouseX,mouseY,80,80)
      elif(keyPressed and key=='k'):
          blendMode(SCREEN)
      elif(keyPressed and key=='l'):
          blendMode(REPLACE)
      elif(keyPressed and key=='z'):
          background(0)
      elif(keyPressed and key=='q'and mouseX==i):
          drawFlower(mouseX,mouseY,30)
      elif(keyPressed and key=='w'and mouseX==i):
          strokeJoin(ROUND)
          drawHeart(mouseX,mouseY,3)
      elif(keyPressed and key=='e'and mouseX==i):
          drawTwinkleStar(mouseX,mouseY,30)

    

# お花スタンプ
def drawFlower(flowerX,flowerY,flowerSize):
    pushMatrix()
    translate(flowerX,flowerY)
    beginShape()
    for theta in range(360):
        R = flowerSize * abs(sin(radians(theta*5))) + flowerSize/2
        x = R * cos(radians(theta))
        y = R * sin(radians(theta))
        
        curveVertex(x,y)
    endShape(CLOSE)
    popMatrix()
            
            
# ハートスタンプ
def drawHeart(heartX,heartY,heartSize):
    pushMatrix()
    translate(heartX,heartY)
    beginShape()
    for theta in range(360):
        x = heartSize * (16 * sin(radians(theta)) * sin(radians(theta)) * sin(radians(theta)))
        y = (-1) * heartSize * (13 * cos(radians(theta)) - 5 * cos(radians(2 * theta)) - 2 * cos(radians(3 * theta)) - cos(radians(4 * theta)))
        
        vertex(x,y)
    endShape(CLOSE)
    popMatrix()
    
    
# キラキラスタンプ
def drawTwinkleStar(starX, starY, starSize):
    pushMatrix()
    translate(starX, starY)
    beginShape()
    for theta in range(360):
        vertex(starSize * pow(cos(radians(theta)), 3), starSize * pow(sin(radians(theta)), 3))
    endShape(CLOSE)
    popMatrix()

    
# イラストを保存
def save_illust():
    global save_count, text_display, text_timer
    if key=='x':
        save("image_"+str(save_count)+".jpg")
        print(u"%s枚目を保存しました。保存したイラストでアニメーションを作成したい際は、Cキーを押してください。\n" % (save_count))
        save_count+=1
            

# イラストの読み込み
def load_images():
    global save_count,images, mode
    for i in range(save_count-1):
        img = loadImage("image_" + str(i+1) + ".jpg")
        images.append(img)
    mode = 'animation'
            
            
# アニメーションの描画    
def draw_animation():
    global frame_count,save_count,images
    background(0)
    
    # フレーム数計算（秒/60倍)
    total_frames = len(images) * 10
    
    # 現在のフレームを計算
    current_frame = frame_count % total_frames
    
    # フレーム範囲ごとに画像を切り替え
    image_index = int(current_frame / 10)
    image(images[image_index],0,0)

    
    
    
def keyPressed():
    global color_mode, red, green, blue, mode, save_count, images
    save_illust()
    
    if key == 'n':
        color_mode = 'rainbow'
        print(u"カラーモードをレインボーモードに切り替えました。\n")
    elif key == 'm':
        color_mode = 'random'
        red = random(255)
        green = random(255)
        blue = random(255)
        print(u"カラーモードをランダムモードに切り替えました。Mキーを押すごとに、グラデーションが変わります。再びレインボーモードに切り替えたい際は、Nキーを押してください。\n")
    elif key == 'c':
        if save_count != 1:
            load_images()
            print(u"アニメーションを再生しています。描画モードに切り替えたい際は、Vキーを押してください。新しいアニメーションを作成したい際は、Vキーの後にBキーを押してください。\n")
        else :
            print(u"Xキーでイラストを保存してから、再度Cキーを押してください。\n")
    elif key == 'v':
        mode = 'draw'
        print(u"描画モードに切り替えました。アニメーションを再生したい際は、Cキーを押してください。\n")
    elif key == 'b':
        save_count = 1
        images = []
        print(u"保存したイラストをリセットしました。新たなアニメーションを作成しましょう！\n")
    elif key == 'k':
        print(u"キラキラペンを選択しました。ふつうのペンや消しゴムに切り替えたい際は、Lキーを押してください。\n")
    elif key == 'l':
        print(u"ふつうのペンを選択しました。\n")
        
        
# キーが離されたときの処理
def keyReleased():

    if key == 'x': 
        saveFrame("animation/frames/######.png")



    
