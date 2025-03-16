from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session, dashboard
from supertokens_python.recipe.emailpassword import InputFormField

from supertokens_python.recipe import usermetadata

from dotenv import load_dotenv
load_dotenv()
import os


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
                form_fields=[InputFormField(id='firstname'), InputFormField(id='lastname'), InputFormField(id='accountID'), InputFormField(id='username')]
            )
        ),
        usermetadata.init(),
    ],
    mode='asgi' # use wsgi if you are running django server in sync mode
)