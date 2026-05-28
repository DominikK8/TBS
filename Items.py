from TBS import Item
import text

ALL_ITEMS = {
    "MATCHBOX": Item(
        flag_name="ITEM_MATCHBOX",
        name=text.MATCHBOX_NAME,
        item_desc=text.MATCHBOX_DESC,
        item_reaktion=text.MATCHBOX_REACT,
        used_flag="MATCHBOX_USED",
        solves= ["BLOCK_REDBUG"]
    ),
    "AIDA": Item(
        flag_name="ITEM_AIDA",
        name=text.AIDA_NAME,
        item_desc=text.AIDA_DESC,
        item_reaktion=text.AIDA_REACT,
        used_flag="AIDA_USED"
    ),
    "DOOR": Item(
        flag_name="ITEM_DOOR",
        name=text.DOOR_NAME,
        item_desc=text.DOOR_DESC,
        item_reaktion=text.DOOR_REACT,
        used_flag="DOOR_USED"
    ),
    "KEY": Item(
        flag_name="ITEM_KEY",
        name=text.KEY_NAME,
        item_desc=text.KEY_DESC,
        item_reaktion=text.KEY_REACT,
        used_flag="KEY_USED"
    ),
    "DOCUMENT": Item(
        flag_name="ITEM_DOCUMENT",
        name=text.DOCUMENT_NAME,
        item_desc=text.DOCUMENT_DESC,
        item_reaktion=text.DOCUMENT_REACT,
        used_flag="DOCUMENT_USED"
    ),
}
