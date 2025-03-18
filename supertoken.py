from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session, dashboard
from supertokens_python.recipe.emailpassword import InputFormField

from dotenv import load_dotenv
load_dotenv()
import os

from supertokens_python import init, InputAppInfo
from supertokens_python.recipe import emailpassword, session
from supertokens_python.recipe.emailpassword.interfaces import (
    APIInterface,
    APIOptions,
    SignUpPostOkResult,
)
from supertokens_python.recipe.emailpassword.types import FormField
from typing import List, Dict, Any, Union
from supertokens_python.recipe.session.interfaces import SessionContainer

def override_email_password_apis(original_implementation: APIInterface):
    original_sign_up_post = original_implementation.sign_up_post

    async def sign_up_post(
        form_fields: List[FormField],
        tenant_id: str,
        session: Union[SessionContainer, None],
        should_try_linking_with_session_user: Union[bool, None],
        api_options: APIOptions,
        user_context: Dict[str, Any],
    ):
        # First we call the original implementation of sign_up_post.
        response = await original_sign_up_post(
            form_fields,
            tenant_id,
            session,
            should_try_linking_with_session_user,
            api_options,
            user_context,
        )

        # Post sign up response, we check if it was successful
        if isinstance(response, SignUpPostOkResult):
            for item in form_fields:
                if (item.id == "firstname"):
                    firstname = item.value
                if (item.id == "lastname"):
                    lastname = item.value
                if (item.id == "username"):
                    username = item.value
            
            print(firstname, lastname, username)

            print("Here")

            ## New SignUp custom logic goes here!
            user_id = response.session.user_id

            # Store user_id, firstname, lastname, accountID, username

            pass
            # TODO: use the input form fields values for custom logic
        else:
            print("NotOk")
        
        return response

    original_implementation.sign_up_post = sign_up_post
    return original_implementation

from supertokens_python.recipe import usermetadata

init(
    # debug=True,
    app_info=InputAppInfo(
        app_name="maubay",
        api_domain=os.environ.get('API_DOMAIN'),
        website_domain=os.environ.get('WEBSITE_DOMAIN'),
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        # We use try.supertokens for demo purposes.
        # At the end of the tutorial we will show you how to create
        # your own SuperTokens core instance and then update your config.
        connection_uri=os.environ.get('CoreConnection'),
        api_key=os.environ.get('CoreAPI')
    ),
    framework='django',
    recipe_list=[
        dashboard.init(),
	    session.init(), # initializes session features
        emailpassword.init(
            sign_up_feature=emailpassword.InputSignUpFeature(
                form_fields=[InputFormField(id='firstname'), InputFormField(id='lastname'), InputFormField(id='username')]
            ),
            override=emailpassword.InputOverrideConfig(
                apis=override_email_password_apis
            ),
        )],
    mode='asgi' # use wsgi if you are running django server in sync mode
)