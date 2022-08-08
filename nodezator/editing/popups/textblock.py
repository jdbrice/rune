
### local imports

from config import APP_REFS

from menu.main import MenuManager

from editing.popups.constants import GeneralPopupCommands

from graphman.textblock.main import TextBlock


class TextBlockPopupMenu(GeneralPopupCommands):

    def __init__(self):

        super().__init__()

        menu_list = [

          {
             'label'  : "Edit text",
             'icon'   : 'text_editing',
             'command': self.edit_block_text,
          },

        ] + self.SINGLE_COMMANDS

        self.text_block_only_popup = (

          MenuManager(

            menu_list,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

        ###

        self.text_block_and_node_in_selected_popup = (

          MenuManager(

            (
              menu_list
              + self.NODE_INCLUSIVE_COLLECTIVE_COMMANDS
            ),

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

        self.text_block_and_no_node_in_selected_popup = (

          MenuManager(

            menu_list + self.COLLECTIVE_COMMANDS,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

    def show(self, text_block, mouse_pos):

        self.obj_under_mouse = text_block

        selected = APP_REFS.ea.selected_objs

        if text_block in selected:

            if any(
              obj
              for obj in selected
              if not isinstance(obj, TextBlock)
            ):

                (
                  self
                  .text_block_and_node_in_selected_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

            else:

                (
                  self
                  .text_block_and_no_node_in_selected_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

        else: (
                self
                .text_block_only_popup
                .focus_if_within_boundaries(mouse_pos) 
              )

    def edit_block_text(self):

        APP_REFS.ea.deselect_all()

        APP_REFS.ea.add_obj_to_selection(
          self.obj_under_mouse
        )

        APP_REFS.ea.edit_text_of_selected()
