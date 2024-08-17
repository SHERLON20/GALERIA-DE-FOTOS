import flet as ft 
def image(num:int):
    return ft.Image(
                src=f"https://picsum.photos/150/150?{num}",#comando acessando as fotos nesse link que é uma api para fotos
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                
            )
def main (page:ft.page):
    page.bgcolor=ft.colors.BLACK
    def new_tela(e):
        btn1.style=btn
        btn2.style=btn
        e.control.style=btn_select
        btn1.update()
        btn2.update()
        if e.control.text == 'agrupadas':
            layout.controls[0]=grid2
        elif e.control.text == 'todas as fotos':
            layout.controls[0]=grid1
        layout.update()

    grid1=ft.GridView(
        
        controls=[#parametro obrigatório de criação.
           image(num)for num in range(4,44)#laco de repetição para renderizar as fotos do link onde esta a variavel
        ],
        expand=True,#comando para as imagens expandirem e ocuparem mais a tela o possivel
        max_extent=150,#comando para definir quantos pixls tera a largura das imagens,para a gradeficar mais dinamica e ajustavel.
        runs_count=5,#comando para definir quantas imagens aparecem por linha passada no parametro
        spacing=5,#comando para definir o espaco de uma linha de imagens para a outra de cima pra baixo
        run_spacing=5,#comando para definir o espacamento da imagens lado a lado.
    )
    grid2=ft.Column(
        expand=True,
        scroll=True,
        controls=[
            ft.Text(value="2022",size=30,color=ft.colors.WHITE),
            ft.GridView(
                controls=[image(num)for num in range(4,7)],
                child_aspect_ratio=1.0,
                spacing=3,
                runs_count=3,
                run_spacing=3,
            ),
            ft.Text(value="2023",size=30,color=ft.colors.WHITE),
            ft.GridView(
                controls=[image(num)for num in range(8,11)],
                child_aspect_ratio=1.0,
                spacing=3,
                runs_count=3,
                run_spacing=3,
            ),
            ft.Text(value="2024",size=30,color=ft.colors.WHITE),
            ft.GridView(
                controls=[image(num)for num in range(41,44)],
                child_aspect_ratio=1.0,
                spacing=3,
                runs_count=3,
                run_spacing=3,
            ),
        ]
    )
    btn_select=ft.ButtonStyle(
        bgcolor=ft.colors.BLACK54,
        color=ft.colors.WHITE,
        elevation=0,
        overlay_color=ft.colors.WHITE12,
        
    )
    btn=ft.ButtonStyle(
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        elevation=0,
        overlay_color=ft.colors.BLACK12,
    )
    footer=ft.Container(#conteiner so recebe um unico componente do flet por isso a row que é pra lista
        margin=ft.margin.symmetric(vertical=5,horizontal=2),
        padding=ft.padding.all(2),
        border_radius=ft.border_radius.all(5),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLACK54,ft.colors.BLACK],
        ),
        content=ft.Row(#parametro para listas no flet
            alignment=ft.MainAxisAlignment.CENTER,
            
            controls=[
               btn1:= ft.ElevatedButton(
                   text="todas as fotos",
                   style=btn_select,
                   on_click=new_tela),
                btn2:=ft.ElevatedButton(
                    text="agrupadas",
                    style=btn,
                    on_click=new_tela,),
            ],
            tight=True
        )
        
    )
    layout=ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            grid1,
            footer,
        ]
    )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main)