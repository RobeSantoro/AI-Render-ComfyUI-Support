import os
import platform
import bpy
import pprint
from colorama import Fore

from . import utils
from .properties_comfy import create_props_from_workflow
from .sd_backends import comfyui_api

from .sd_backends.comfyui_api import (
    COMFY_WORKFLOWS,
    COMFY_CKPT_MODELS,
    COMFY_LORA_MODELS,
    COMFY_CONTROL_NETS,
    COMFY_UPSCALE_MODELS,
)


class AIR_OT_open_comfyui_input_folder(bpy.types.Operator):
    "Open the input folder in the windows explorer or macOSfinder"
    bl_idname = "ai_render.open_comfyui_input_folder"
    bl_label = "Open Output Folder"

    def execute(self, context):
        input_folder = comfyui_api.get_comfyui_input_path(context)
        print(f"Opening folder: {input_folder}")

        if platform.system() == "Windows":
            os.system(f"start {input_folder}")
        elif platform.system() == "Darwin":
            os.system(f"open {input_folder}")

        return {'FINISHED'}


class AIR_OT_open_comfyui_output_folder(bpy.types.Operator):
    "Open the output folder in the windows explorer or macOSfinder"
    bl_idname = "ai_render.open_comfyui_output_folder"
    bl_label = "Open Output Folder"

    def execute(self, context):
        output_folder = comfyui_api.get_comfyui_output_path(context)
        print(f"Opening folder: {output_folder}")

        if platform.system() == "Windows":
            os.system(f"start {output_folder}")
        elif platform.system() == "Darwin":
            os.system(f"open {output_folder}")

        return {'FINISHED'}


class AIR_OT_open_comfyui_workflows_folder(bpy.types.Operator):
    "Open the workflow folder in the windows explorer or macOSfinder"
    bl_idname = "ai_render.open_comfyui_workflows_folder"
    bl_label = "Open Workflow Folder"

    def execute(self, context):
        workflow_folder = utils.get_addon_preferences().comfyui_workflows_path
        print(f"Opening folder: {workflow_folder}")

        if platform.system() == "Windows":
            os.system(f'explorer "{workflow_folder}"')
        elif platform.system() == "Darwin":
            os.system(f"open {workflow_folder}")

        return {'FINISHED'}


# class AIR_OT_UpdateWorkflowEnum(bpy.types.Operator):
#     bl_idname = "ai_render.update_workflow_enum"
#     bl_label = "Update Workflow Enum"
#     bl_description = "Update the workflow enum with the available workflows"

#     def execute(self, context):
#         print(Fore.GREEN + "UPDATING WORKFLOW ENUM..." + Fore.RESET)

#         global COMFY_WORKFLOWS
#         COMFY_WORKFLOWS.clear()
#         workflows_list = comfyui_api.get_workflows(context)  # Ensure comfyui_api is available
#         for workflow in workflows_list:
#             COMFY_WORKFLOWS.append(workflow)

#         # Trigger the update of the update of the enums before setting the new values
#         bpy.ops.ai_render.update_ckpt_enum()
#         bpy.ops.ai_render.update_lora_enum()
#         bpy.ops.ai_render.update_control_net_enum()

#         # Trigger property creation from the selected workflow
#         create_property_from_workflow(context.scene.comfyui_props, context)

#         # comfui_props = context.scene.comfyui_props
#         # string_enum_mapping_dict = {
#         #     "comfyui_checkpoint_loader_simple": {
#         #         "ckpt_name": "ckpt_enum"
#         #     },
#         #     "comfyui_lora_nodes": {
#         #         "lora_name": "lora_enum"
#         #     }
#         # }

#         # for prop in comfui_props.bl_rna.properties.items():
#         #     if (
#         #         prop[1].type == 'COLLECTION'
#         #         and getattr(comfui_props, prop[0])  # Check if the collection has items
#         #         and prop[0] in string_enum_mapping_dict.keys()  # Check if the collection is in the enum_to_set dict
#         #     ):
#         #         collection_property = prop[0]
#         #         current_property_name, enum_property_name = next(iter(string_enum_mapping_dict[collection_property].items()))

#         #         for item in getattr(comfui_props, collection_property):
#         #             new_value = getattr(item, current_property_name)
#         #             setattr(item, enum_property_name, new_value)  # Set the item's enum property to the corresponding string property
#         #             print(Fore.GREEN + f"Setting {enum_property_name} of {collection_property} to {current_property_name}" + Fore.RESET)

#         return {'FINISHED'}


class AIR_OT_UpdateSDModelEnum(bpy.types.Operator):
    bl_idname = "ai_render.update_ckpt_enum"
    bl_label = "Update Model Enum"
    bl_description = "Update the model enum with the available models"

    def execute(self, context):
        print(Fore.MAGENTA + "\nUPDATING SD MODEL ENUM..." + Fore.RESET)
        global COMFY_CKPT_MODELS
        COMFY_CKPT_MODELS.clear()
        models_list = comfyui_api.get_ckpt_models(context)
        for model in models_list:
            COMFY_CKPT_MODELS.append(model)

        return {'FINISHED'}


class AIR_OT_UpdateLoraModelEnum(bpy.types.Operator):
    bl_idname = "ai_render.update_lora_enum"
    bl_label = "Update Model Enum"
    bl_description = "Update the model enum with the available models"

    def execute(self, context):
        print(Fore.YELLOW + "\nUPDATING LORA MODEL ENUM..." + Fore.RESET)
        global COMFY_LORA_MODELS
        COMFY_LORA_MODELS.clear()
        models_list = comfyui_api.get_lora_models(context)
        for model in models_list:
            COMFY_LORA_MODELS.append(model)

        return {'FINISHED'}


class AIR_OT_UpdateControlNetEnum(bpy.types.Operator):
    bl_idname = "ai_render.update_control_net_enum"
    bl_label = "Update Control Net Enum"
    bl_description = "Update the control net enum with the available control nets"

    def execute(self, context):
        print(Fore.BLUE + "\nUPDATING CONTROL NET ENUM..." + Fore.RESET)
        global COMFY_CONTROL_NETS
        COMFY_CONTROL_NETS.clear()
        control_nets_list = comfyui_api.get_control_nets(context)
        for control_net in control_nets_list:
            COMFY_CONTROL_NETS.append(control_net)

        return {'FINISHED'}


class AIR_OT_UpdateUpscaleModelEnum(bpy.types.Operator):
    bl_idname = "ai_render.update_upscale_model_enum"
    bl_label = "Update Upscale Model Enum"
    bl_description = "Update the upscale model enum with the available models"

    def execute(self, context):
        print(Fore.CYAN + "\nUPDATING UPSCALE MODEL ENUM..." + Fore.RESET)
        global COMFY_UPSCALE_MODELS
        COMFY_UPSCALE_MODELS.clear()
        upscale_models_list = comfyui_api.get_upscale_models(context)
        for upscale_model in upscale_models_list:
            COMFY_UPSCALE_MODELS.append(upscale_model)

        return {'FINISHED'}


classes = [
    AIR_OT_UpdateSDModelEnum,
    AIR_OT_UpdateLoraModelEnum,
    AIR_OT_UpdateControlNetEnum,
    AIR_OT_UpdateUpscaleModelEnum,
    AIR_OT_open_comfyui_input_folder,
    AIR_OT_open_comfyui_output_folder,
    AIR_OT_open_comfyui_workflows_folder,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
